from flask import Flask, jsonify
import os
from app.scraper import scrape_and_summarize
from app.emailer import send_email

app = Flask(__name__)

@app.route('/scrape')
def scrape_route():
    try:
        results = scrape_and_summarize()
        if results:
            subject = "Surf Ratings Found!"
            body = "\n\n".join(results)
            send_email(subject, body, os.environ.get("NOTIFY_EMAIL"))
            return jsonify({"status": "email sent", "details": results})
        else:
            return jsonify({"status": "no ratings found"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
