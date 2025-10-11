import requests
from bs4 import BeautifulSoup

def scrape_jobs(keyword):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/125.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    url = f"https://www.indeed.com/jobs?q={keyword.replace(' ', '+')}&l="
    print(f"[DEBUG] Scraping: {url}")

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"[ERROR] Failed to fetch page: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    job_cards = soup.select("div.job_seen_beacon")
    if not job_cards:
        print("[INFO] No job cards found on page — maybe dynamic JS loading or blocked request.")
        return []

    jobs = []
    for card in job_cards[:10]:  # Limit to first 10 results
        title_tag = card.select_one("h2.jobTitle span")
        title = title_tag.text.strip() if title_tag else "N/A"

        company_tag = card.select_one("span.companyName")
        company = company_tag.text.strip() if company_tag else "N/A"

        location_tag = card.select_one("div.companyLocation")
        location = location_tag.text.strip() if location_tag else "N/A"

        salary_tag = card.select_one("div.salary-snippet")
        salary = salary_tag.text.strip() if salary_tag else "Not mentioned"

        url_tag = card.select_one("a")
        job_url = f"https://www.indeed.com{url_tag['href']}" if url_tag and url_tag.get("href") else "#"

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "salary": salary,
            "url": job_url,
        })

    print(f"[INFO] Extracted {len(jobs)} jobs")
    return jobs
