# Tech Job Scraper

A simple web-based **Tech Job Scraper** built with Python and Flask that collects job listings from selected sources and presents them through a clean web interface. The project is designed to demonstrate web scraping, backend routing, and basic frontend integration in a structured, extensible way.

---

## 🚀 Features

* Scrapes tech-related job listings from supported websites
* Flask-based backend with clear project separation
* Clean HTML templates with custom CSS styling
* Modular scraper logic for easy extension
* Ready for authentication or database expansion

---

## 📁 Project Structure

```
tech-job-scraper/
│
├── static/
│   ├── auth.js          # Frontend authentication logic (JS)
│   ├── scraper.css      # Styles specific to scraper views
│   └── styles.css       # Global styles
│
├── templates/            # HTML templates (Jinja2)
│
├── app.py                # Main Flask application entry point
├── config.py             # Configuration settings
├── models.py             # Database models (optional / extensible)
├── scraper.py            # Core job scraping logic
├── requirements.txt      # Python dependencies
└── .gitignore            # Git ignore rules
```

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Web Scraping:** BeautifulSoup / Requests (or similar)
* **Frontend:** HTML, CSS, JavaScript
* **Templating:** Jinja2

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/tech-job-scraper.git
   cd tech-job-scraper
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. Open your browser and navigate to:

   ```
   http://127.0.0.1:5000
   ```

---

## 🧠 How It Works

* `scraper.py` handles fetching and parsing job data from target websites
* `app.py` manages routes and sends scraped data to templates
* `templates/` renders the job listings dynamically
* `static/` contains all frontend assets (CSS & JS)

---

## 🔮 Future Improvements

* Add user authentication and saved job lists
* Store scraped jobs in a database
* Support multiple job platforms
* Add filters (location, role, experience)
* Schedule automated scraping

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👤 Author
By Murali Krishna M
Developed as a learning and portfolio project to showcase full-stack fundamentals and web scraping techniques.
