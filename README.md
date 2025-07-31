📄 Rozee.pk Job Listing Scraper (Selenium Based)

This is an automated job scraper built with **Python** and **Selenium**. It extracts job listings from [Rozee.pk](https://www.rozee.pk) using browser automation techniques.
"Built with Selenium — encountered advanced bot-detection which led me to explore better tools like Playwright."
🔧 Technologies Used

- 🐍 Python 3
- 🧪 Selenium WebDriver
- 🌐 Chrome (with randomized User-Agent support)
- 📦 Virtual Environment (`myenv`)
- 📝 HTML parsing (planned in next versions)

---
💡 Features

- ✅ Random User-Agent to reduce bot detection
- ✅ Dynamic wait handling with `time.sleep`
- ✅ Organized code with functions (`create_driver`, etc.)
- ✅ Ready for upgrade to Playwright or BeautifulSoup
- ✅ Can save scraped HTML for further parsing

📌 Project Progress
✅ Selenium Setup Done
Headless disabled
Custom user-agent added
Random delays inserted
HTML source captured

❌ Job Data Not Loaded

Rozee dynamically renders job listings
Blocks Selenium bots
Job cards = 0 found

🔄 Switching to Playwright
Better stealth + dynamic content support
Using async version for performance
Plan to extract multiple pages
