# 🕸️ Python Web Crawler – W3Schools & Dynamic Sites

This is a Python-based web crawler capable of scraping both **static** and **dynamic** websites. It supports interactive navigation of HTML structures, allowing users to explore topics like Python tutorials on W3Schools and even scrape JavaScript-rendered content such as Digikala's grocery search page.

---

## 🌐 Features

- 📄 **Static Site Crawling** using `requests` + `BeautifulSoup`
  - Navigates W3Schools Python sections
  - Interactive CLI menu for choosing topics and subtopics
- ⚡ **Dynamic Site Crawling** using `pyppeteer` (Headless Chromium)
  - Supports JavaScript-rendered pages (e.g., Digikala)
- 🔍 Extracts content from structured menus and hyperlinks
- 🧭 Gracefully handles HTML comments, siblings, and nested sections
- 🧪 Clean utility functions for input, URL resolution, and tag parsing

---

## 🧰 Tech Stack

- Python 3.x
- [Requests](https://pypi.org/project/requests/) – For HTTP requests
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) – For parsing HTML
- [Pyppeteer](https://github.com/pyppeteer/pyppeteer) – Headless Chromium automation (like Puppeteer)
- [asyncio](https://docs.python.org/3/library/asyncio.html) – For running async tasks

---
