# Surf Forecast Scraper

This project is a Python-based web scraper that checks surf ratings from [surf-forecast.com](https://www.surf-forecast.com) and sends email notifications when favorable conditions are found.

## 🧰 Features

- Scrapes surf ratings (2–5 stars) for multiple beaches.
- Filters ratings only from the first 9 forecast cells.
- Sends email notifications via Gmail SMTP.
- Deployable to Google Cloud Run on a schedule.
- Needs docker image which may be 2 gig and above 
- Docker image is above the free tier for Artifact Registry API
- other charges can apply if the image is accessed etc

## 🔧 Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt