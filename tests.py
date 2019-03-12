from selenium import webdriver

from pages.category_page import CategoryPage

# Test Setup
browser = webdriver.Chrome()

# Items in Category Drop Down Menu test
category_page = CategoryPage(driver=browser)
category_page.go()
print(category_page.category_dropdown.options)

input()
browser.quit()
