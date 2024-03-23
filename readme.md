# Dev.to Article Scraper

Welcome to Dev.to Article Scraper, a Django-powered web scraper designed to extract articles from Dev.to!

## Introduction

This project utilizes Celery, Selenium, and Redis to scrape articles from Dev.to published within the last four years under a specified search term. The extracted articles are displayed in a convenient table format, showcasing the title, link, and publication date. The "Scrape History" section in the navbar presents timestamps for all previous scrape attempts, along with a "Scrape" button to initiate asynchronous scraping of Dev.to. Bootstrap is employed for styling, while pagination and search functionalities enhance the user experience.

## Getting Started

To set up the project:

1. Ensure Redis is installed and running (listening on localhost:6379)

2. Install all dependencies listed in requirements.txt. The project requires Python 3.12.

`pip install -r requirements.txt`

3. After installing dependencies, migrate the database and start the Django server:

`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py runserver`

4. In a separate terminal, launch the Celery worker:

`celery -A newsscraper worker -l info`

5. Once these steps are completed, navigate to the "Scrape History" tab and press the "Scrape" button to initiate the web scraping process. The results will be displayed on the home page.

## Technologies used

- **Django**: Django framework powers the backend development of the project.
- **Celery**: Celery is used for task queue implementation.
- **Selenium**: Selenium automates web browser interaction for scraping.
- **Redis**: Redis serves as the broker for Celery.
- **Bootstrap**: Bootstrap framework is utilized for frontend styling.

## About the Author

This project is maintained by **Oliver Wood**. Connect with me on [LinkedIn](https://www.linkedin.com/in/olijwood)!

## Thank You

Thank you for your interest in this web scraping project! I hope you find it useful and informative. Happy scraping!