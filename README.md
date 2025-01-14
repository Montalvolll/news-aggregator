# News Aggregator App

The **News Aggregator App** is a simple web application built with Flask. It allows users to fetch and filter news articles from various RSS feeds using specific keywords and date ranges.

---

## Features
- Fetch articles from predefined RSS feeds.
- Filter articles by keywords and publication date (e.g., today, last 3 days).
- Display articles with source name, title, keywords, link, and publication date.
- Simple and interactive UI built with HTML and Bootstrap.

---

## Directory Structure
```plaintext
news-feeder/
├── app/
│   ├── templates/
│   │   └── index.html       # Frontend of the app
│   ├── app.py               # Main Flask application
│   └── requirements.txt     # Python dependencies
├── Dockerfile               # Docker configuration file
└── README.md                # Documentation (this file)
```

---

## Requirements
- Python 3.7+
- pip (Python package manager)
- Docker (optional for containerization)

---

## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/news-aggregator.git
   cd news-feeder
   ```

2. Navigate to the `app/` directory:
   ```bash
   cd app
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app locally:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## Dockerizing the App

### 1. Create Docker Image

1. Ensure the following files exist in the root directory:
   - `Dockerfile`
   - `requirements.txt`

2. Build the Docker image:
   ```bash
   docker build -t news-aggregator-app .
   ```

### 2. Run Docker Container

1. Run the container and expose it on port 5000:
   ```bash
   docker run -d -p 5000:5000 news-aggregator-app
   ```

2. Access the app in your browser:
   ```
   http://localhost:5000
   ```

---

## Example Usage
1. Add keywords in the input field to filter news articles.
2. Select a date range (e.g., "Last 3 Days").
3. Click **Get News** to fetch articles.
4. View the results, which include:
   - Source name
   - Article title
   - Keywords matched
   - Link to the article
   - Published date

---

## Known Issues & Recommendations
1. **Rate Limiting**: The app fetches feeds dynamically. Implement rate-limiting to prevent abuse.
2. **Feed Validation**: Ensure feeds are trusted and sanitized to avoid malicious content.
3. **Scalability**: Use a production-ready WSGI server like Gunicorn for large-scale deployment.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch and submit a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For questions or feedback, contact [https://linkedin.com/.](https://www.linkedin.com/in/josemmontalvo/)
