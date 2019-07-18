from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_search_add_to_cart_button(browser):
    browser.get(link)
    sleep(30)
    browser.find_element_by_class_name("btn-add-to-basket")
