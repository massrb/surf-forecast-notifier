from scraper import scrape_and_summarize

if __name__ == '__main__':
    results = scrape_and_summarize()
    if results:
        for r in results:
            print(r)
    else:
        print("No ratings found.")
