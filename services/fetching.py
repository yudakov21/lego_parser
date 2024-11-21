from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.conf import settings

def fetch_dynamic_page(url):
    # Запускаем Selenium с вашими настройками
    driver = webdriver.Firefox(options=settings.FIREFOX_OPTIONS, executable_path=settings.EXECUTABLE_PATH)
    try:
        driver.get(url)
        # Ожидаем появления товаров
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-test="product-item"]'))
        )
        # Получаем HTML-код страницы
        page_content = driver.page_source
    finally:
        driver.quit()  # Закрываем браузер
    return page_content
