from selenium import webdriver


def edge_browser():
    browser = webdriver.Edge()
    yield browser
    
    # Teardown
    print("I'am tearing down this browser")
    