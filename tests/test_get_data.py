import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_data():
    # Configure the Selenium driver (in this case, we'll use Edge)
    browser = webdriver.Chrome()

    # Open the Forbes website
    browser.get("https://www.forbes.com/")

    time.sleep(5)
    # Locate the "Menu" button and click it
    menu_button = browser.find_element(By.ID, "header-dropdown-button")
    menu_button.click()

    # Locate the "Tech" option in the dropdown menu and click it
    tech_option = browser.find_element(By.LINK_TEXT, "Innovation")
    tech_option.click()

    # Wait for a moment to ensure the technology page is fully loaded
    browser.implicitly_wait(10)

    # Locate the top 10 tech news articles
    tech_news_elements = browser.find_elements(By.CSS_SELECTOR, ".simple-item-list h2 a")

    # Extract and print the titles of the news articles
    for index, tech_news in enumerate(tech_news_elements[:10], start=1):
        print(f"{index}. {tech_news.text}")

    # Close the browser
    browser.quit()


# def test_get_data():
    
if __name__ == '__main__':
    get_data()