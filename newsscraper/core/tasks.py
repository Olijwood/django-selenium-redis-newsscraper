from celery import shared_task
import time
from .scrapers import scrape
# allows you to call this function asynchronously
URL = 'https://dev.to/search?q=django'

@shared_task
def scrape_async():
    scrape(URL)
    return