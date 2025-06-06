from playwright.sync_api import sync_playwright
import time
from collections import Counter

def scrape_and_summarize():
    
    with open("urls.txt") as f:
        urls = [line.strip() for line in f if line.strip()]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        results = []

        for url in urls:
            page.goto(url, wait_until='domcontentloaded')
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)

            try:
                page.wait_for_selector('.star-rating__rating--2', timeout=10000)
            except Exception:
                continue

            cells = page.query_selector_all('.forecast-table__cell--has-image')[:9]
            ratings = []
            for cell in cells:
                found = cell.query_selector(
                    '.star-rating__rating--2, '
                    '.star-rating__rating--3, '
                    '.star-rating__rating--4, '
                    '.star-rating__rating--5'
                )
                if found:
                    ratings.append(found)

            rating_counts = Counter()
            for r in ratings:
                classes = r.get_attribute("class")
                rating_num = None
                if classes:
                    for cls in classes.split():
                        if cls.startswith("star-rating__rating--"):
                            rating_num = cls.split("--")[-1]
                            break
                if rating_num:
                    rating_counts[rating_num] += 1

            if rating_counts:
                summary = ", ".join(f"{num} Stars ({count})" for num, count in sorted(rating_counts.items()))
                results.append(f"URL: {url}\nSummary: {summary}\n")

        browser.close()
    return results
