from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Job
from scraper import scrape_jobs

app = Flask(__name__)
app.config.from_object(Config)

# Initialize db with app
db.init_app(app)

with app.app_context():
    db.create_all()

# Login page route
@app.route('/')
def login():
    return render_template('index.html')  # Changed from login.html to index.html

# Signup page route  
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Scraper page route (main application)
@app.route('/scraper', methods=['GET', 'POST'])
def scraper():
    jobs = []
    search_query = ""
    
    try:
        if request.method == 'POST':
            search_query = request.form.get('query', '').strip()
            print(f"Search query: {search_query}")
            
            if search_query:
                # Scrape new jobs
                scraped_jobs = scrape_jobs(search_query)
                print(f"Scraped {len(scraped_jobs)} jobs for '{search_query}'")
                
                # Save scraped jobs to DB
                for job_data in scraped_jobs:
                    # Check if job already exists to avoid duplicates
                    existing_job = Job.query.filter_by(
                        title=job_data['title'],
                        company=job_data['company'],
                        url=job_data['url']
                    ).first()
                    
                    if not existing_job:
                        new_job = Job(
                            title=job_data['title'],
                            company=job_data['company'],
                            location=job_data['location'],
                            salary=job_data['salary'],
                            url=job_data['url']
                        )
                        db.session.add(new_job)
                
                db.session.commit()
                print("Jobs saved to database")
        
        # Get jobs from database - filter by search query if provided
        if search_query:
            jobs = Job.query.filter(
                Job.title.ilike(f'%{search_query}%') | 
                Job.company.ilike(f'%{search_query}%') |
                Job.location.ilike(f'%{search_query}%')
            ).order_by(Job.date_scraped.desc()).all()
        else:
            # Show all jobs if no search, newest first
            jobs = Job.query.order_by(Job.date_scraped.desc()).all()
            
        print(f"Displaying {len(jobs)} jobs from database")
        
    except Exception as e:
        print(f"Error: {e}")
        jobs = []
    
    return render_template('scraper.html', jobs=jobs, search_query=search_query)

# Simple route to handle login button click
@app.route('/login-submit', methods=['POST'])
def login_submit():
    return redirect(url_for('scraper'))

# Simple route to handle signup button click  
@app.route('/signup-submit', methods=['POST'])
def signup_submit():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)