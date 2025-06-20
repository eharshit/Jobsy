import requests
from bs4 import BeautifulSoup

def scrape_internshala(keyword="python", max_results=10):
    base_url = f"https://internshala.com/internships/keywords-{keyword}/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    internships = []
    listings = soup.find_all("div", class_="individual_internship")[:max_results]

    for listing in listings:
        try:
            # Title & Link
            title_tag = listing.find("a", class_="job-title-href")
            title = title_tag.get_text(strip=True) if title_tag else "N/A"
            link = "https://internshala.com" + title_tag["href"] if title_tag else "N/A"

            # Company Name
            company_tag = listing.find("p", class_="company-name")
            company = company_tag.get_text(strip=True) if company_tag else "N/A"

            # Location
            location_tag = listing.find("div", class_="row-1-item locations")
            location = location_tag.find("a").get_text(strip=True) if location_tag and location_tag.find("a") else "Remote"

            # Stipend
            stipend_tag = listing.find("span", class_="stipend")
            stipend = stipend_tag.get_text(strip=True) if stipend_tag else "N/A"

            # Duration (hacky but works)
            row_items = listing.find_all("div", class_="row-1-item")
            duration = row_items[2].get_text(strip=True) if len(row_items) >= 3 else "N/A"

            internships.append({
                "title": title,
                "company": company,
                "location": location,
                "duration": duration,
                "stipend": stipend,
                "link": link
            })

        except Exception as e:
            print("❌ Skipped one listing due to:", e)

    return internships

# 🔎 Test block
if __name__ == "__main__":
    data = scrape_internshala(keyword="python", max_results=5)
    for i, job in enumerate(data, 1):
        print(f"{i}. {job['title']} at {job['company']}")
        print(f"   📍 {job['location']} | 💰 {job['stipend']} | ⏳ {job['duration']}")
        print(f"   🔗 {job['link']}\n")
