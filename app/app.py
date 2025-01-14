from flask import Flask, render_template, request
from flask_cors import CORS
from datetime import datetime, timedelta
import feedparser

app = Flask(__name__)
CORS(app)

# Example feeds to aggregate
FEEDS = [
    "https://feeds.feedburner.com/TheHackersNews",
    "https://news.ycombinator.com/rss",
    "https://www.darkreading.com/rss.xml",
    "https://www.bleepingcomputer.com/feed/",
    "https://techcrunch.com/feed/",
    "https://threatpost.com/feed/",
    "https://www.cisa.gov/cybersecurity-advisories/all.xml",
    "https://www.cisa.gov/blog.xml",
    "https://www.schneier.com/feed/atom/",
    "https://krebsonsecurity.com/feed/",
    "https://www.securityweek.com/feed/",
    "https://feeds.feedburner.com/Unit42",
    "https://portswigger.net/research/rss",
    "https://msrc.microsoft.com/blog/feed",
    "https://www.hackerone.com/blog.rss",
    "https://www.offsec.com/feed/",
    "https://www.wired.com/feed/category/security/latest/rss",
    "https://feeds.arstechnica.com/arstechnica/index/",
    "https://www.zdnet.com/topic/security/rss.xml",
    "https://grahamcluley.com/feed/",
    "https://www.csoonline.com/feed/",
    "https://www.infosecurity-magazine.com/rss/news/",
    "https://research.checkpoint.com/feed/",
    "http://blog.malwarebytes.org/feed/",
    "https://www.ghacks.net/feed/",
    "https://www.theregister.com/security/headlines.atom",
    "https://securityaffairs.com/feed",
    "https://feeds.feedburner.com/securityweek",
    "https://hackread.com/feed/",
    "https://www.reddit.com/r/netsec/.rss",
    # Add more feed URLs as needed
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/news", methods=["POST"])
def get_news():
    keywords = request.json.get("keywords", [])
    date_filter = request.json.get("date_filter", "")

    filtered_articles = []
    now = datetime.now()

    # Define date ranges
    if date_filter == "today":
        start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
    elif date_filter == "last_24_hours":
        start_date = now - timedelta(days=1)
    elif date_filter == "last_3_days":
        start_date = now - timedelta(days=3)
    elif date_filter == "last_7_days":
        start_date = now - timedelta(days=7)
    elif date_filter == "last_30_days":
        start_date = now - timedelta(days=30)
    else:
        start_date = None

    for feed_url in FEEDS:
        feed = feedparser.parse(feed_url)
        feed_title = feed.feed.title if "title" in feed.feed else "Unknown Source"
        for entry in feed.entries:
            publish_date = (
                datetime(*entry.published_parsed[:6])
                if "published_parsed" in entry
                else None
            )

            if publish_date and start_date and publish_date < start_date:
                continue

            matched_keywords = [
                kw for kw in keywords if kw in (entry.title + str(entry))
            ]
            if keywords and not matched_keywords:
                continue

            highlighted_keywords = ", ".join(matched_keywords)

            filtered_articles.append(
                {
                    "source": feed_title,
                    "title": entry.title,
                    "link": entry.link,
                    "published": (
                        publish_date.strftime("%Y-%m-%d %H:%M:%S")
                        if publish_date
                        else "Unknown"
                    ),
                    "keywords": highlighted_keywords,
                }
            )
    return {"articles": filtered_articles}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
