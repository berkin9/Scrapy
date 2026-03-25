📚 Web Scraping Project

Author: Berkin Akbiyik
Date: July 13, 2023

📌 Overview

This project is a web scraping application developed using Python. It leverages powerful libraries such as Scrapy and PyMongo to extract and store data efficiently.

The application scrapes book-related information from the website kitapyurdu.com, including:

📖 Book Title
✍️ Author
🏢 Publisher
💰 Price
⚙️ Technologies Used
Python
Scrapy
PyMongo
MongoDB
🚀 Features
Automated data extraction from a live e-commerce website
Structured scraping using Scrapy spiders
Seamless integration with MongoDB for data storage
Real-time data persistence during scraping
🗄️ Database

The scraped data is stored in a MongoDB database using the PyMongo library.

You can view the stored data locally by connecting to:

mongodb://localhost:27017


Make sure your MongoDB server is running before starting the application.

▶️ How to Run

Clone the repository:

git clone <your-repo-url>
cd <your-project-folder>


Install dependencies:

pip install -r requirements.txt


Run the scraper:

scrapy crawl <spider_name>

📂 Project Structure (Example)
project/
│── spiders/
│   └── book_spider.py
│── items.py
│── pipelines.py
│── settings.py
│── requirements.txt
│── README.md

📚 Notes
Ensure MongoDB is installed and running locally.
Update the spider name and target URLs as needed.
This project is intended for educational purposes and demonstrates practical usage of web scraping and database integration.

📎 Resources
https://realpython.com/web-scraping-with-scrapy-and-mongodb/#installation
https://www.mongodb.com/try/download/shell
https://www.mongodb.com/try/download/shell
https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
https://www.youtube.com/watch?v=GogxAQ2JP4A&t=1560s
https://www.youtube.com/watch?v=djfnjtYB2co
