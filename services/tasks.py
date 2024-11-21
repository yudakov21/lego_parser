from celery import shared_task
from .parser import LegoParser
from .data_manager import LegoDataManager
from .fetching import fetch_dynamic_page

@shared_task
def scrape_lego_sales():

    url = 'https://www.lego.com/de-de/categories/sales-and-deals'

    # Используем Selenium для получения динамического HTML
    raw_html = fetch_dynamic_page(url)

    parser = LegoParser(raw_html)
    toys = parser.parse_toys()

    LegoDataManager.save_toys(toys)