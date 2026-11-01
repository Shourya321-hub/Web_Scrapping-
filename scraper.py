import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Starting URL
base_url = "https://quotes.toscrape.com/page/{}/"

# Store scraped records
data = []

# Maximum number of pages
max_pages = 10

# Request headers
headers = {
    "User-Agent": "CodeAlpha-Web-Scraping-Project/1.0"
}

for page in range(1, max_pages + 1):

    print(f"Scraping page {page}...")

    url = base_url.format(page)

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

    except requests.RequestException as error:
        print(f"Error accessing page {page}: {error}")
        continue

    # Parse HTML
    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # Find quotes
    quotes = soup.find_all(
        "div",
        class_="quote"
    )

    # Stop if no quotes are found
    if not quotes:
        print("No more quotes found.")
        break

    # Extract data
    for quote in quotes:

        text_element = quote.find(
            "span",
            class_="text"
        )

        author_element = quote.find(
            "small",
            class_="author"
        )

        if text_element is None or author_element is None:
            continue

        text = text_element.get_text(
            strip=True
        )

        author = author_element.get_text(
            strip=True
        )

        tags = quote.find_all(
            "a",
            class_="tag"
        )

        tag_list = []

        for tag in tags:
            tag_list.append(
                tag.get_text(strip=True)
            )

        data.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tag_list)
        })

    # Wait before requesting the next page
    time.sleep(1)


# Convert to DataFrame
df = pd.DataFrame(data)

# Remove duplicate records
df = df.drop_duplicates()

# Save data
df.to_csv(
    "output/quotes.csv",
    index=False
)

print("\n" + "=" * 50)
print("SCRAPING COMPLETED")
print("=" * 50)

print("Total records:", len(df))
print("Total authors:", df["Author"].nunique())

print("\nFile saved:")
print("output/quotes.csv")
