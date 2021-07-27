from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://techstepacademy.com/training-ground")

input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"

#Assign elements
input1_elem = browser.find_element_by_css_selector(input2_css_locator)
butn4_elem = browser.find_element_by_xpath(button4_xpath_locator)

# Manipulate elements
input1_elem.send_keys("Test text")
butn4_elem.click()