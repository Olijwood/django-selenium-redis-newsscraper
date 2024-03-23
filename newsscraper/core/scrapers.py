from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 

import time
import datetime
from dateutil.relativedelta import relativedelta

from .models import NewsItem, ScrapeRecord

def scrape(url):
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)
    print(driver.title)
    timeout = 30
    try:
        time.sleep(2)
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//article[@class='crayons-story']")
            )
        )
        elements = driver.find_elements(By.XPATH, "//article[@class='crayons-story']")
        print('element located')
    except TimeoutException:
        print('Timed out waiting for driver to load')
        driver.quit()

    try: 
        time.sleep(2)
        elements = driver.find_elements(By.XPATH, "//article[@class='crayons-story']")
        for e in elements[0:1]:
                print(e.text)

        for article in elements:
            # try get anchor tag and href
            if article.get_attribute('data-content-user-id') != 'undefined':
                news_item_link = article.find_element(
                    By.XPATH, ".//a[@class='crayons-story__tertiary fs-xs']")
                news_item_href = news_item_link.get_attribute('href')

                # try get title
                title_result = article.find_element(
                    By.TAG_NAME, 'h3')
                news_item_title = title_result.text

                # try get timestamp

                four_years_ago = datetime.date.today() - relativedelta(years=4)

                time_result = article.find_element(
                        By.TAG_NAME, 'time')
                news_item_time = time_result.text

                # convert time text into datetime object
                if "'" in news_item_time:
                        # parse the year
                    news_item_date = datetime.datetime.strptime(
                            news_item_time, "%b %d '%y").date()
                else:
                    # year is the current year
                    news_item_date = datetime.datetime.strptime(
                            news_item_time)
                    today = datetime.date.today()
                    news_item_date = news_item_date.replace(
                            year=today.year).date()
                    
                if news_item_date > four_years_ago:
                    
                    NewsItem.objects.get_or_create(
                        title=news_item_title,
                        link=news_item_href,
                        source='Dev.to',
                        publish_date=news_item_date
                    )
        ScrapeRecord.objects.create()
        
        driver.quit()
    except:
        pass
         # send ourselves email
        print('failed')
        driver.quit()
