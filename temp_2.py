import pytest
from selenium import webdriver

browser = webdriver.Chrome()
#Given: Usr on the following page
browser.get("http://techstepacademy.com/training-ground")

# When: Find text field and input "Test text" text into it
input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"

#Assign elements
element = browser.find_element_by_id('ipt2') #this element is visible
assert element.is_displayed() == True
# if element.is_displayed():
#     assert
#     print "Element found"
# else:
# print "Element not found"