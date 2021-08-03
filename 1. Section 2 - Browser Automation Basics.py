import pytest
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://techstepacademy.com/training-ground")

input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"

#Assign elements
def Test_1(self):
    input1_elem = browser.find_element_by_css_selector(input2_css_locator)
    input1_elem.send_keys("Test text")
    assert True
    assert input1_elem == input2_css_locator
    assert input1_elem == "ipt2"

def Test_2():
    butn4_elem = browser.find_element_by_xpath(button4_xpath_locator)
    butn4_elem.click()
    assert True
    assert butn4_elem == "//button[@id='b4']"

# Manipulate elements