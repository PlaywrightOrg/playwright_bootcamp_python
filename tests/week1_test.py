import pytest
from playwright.sync_api import sync_playwright
from aux_func import login


#acá comenzamos a definir nuestros tests la función tiene que empezar con test para que el
#runner las reconozca 

#Los pasos son los mismos que ustedes hicieron pero separamos la navegación en diferentes funciones
#y agregamos assert para verificar que el test pasó.
def test_login_page(browser):
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_load_state('networkidle')
    page.screenshot(path="Screenshots/Loginpage.png", full_page=True)
    assert page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    page.close()

def test_navigation_and_directory_page(browser):
    page = browser.new_page()
    login(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory")
    page.wait_for_load_state('networkidle')
    page.screenshot(path="Screenshots/Directory.png", full_page=True)
    assert page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory"
    page.close()


def test_employee_list_page(browser):

    page = browser.new_page()
    login(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    page.wait_for_load_state('networkidle')
    page.screenshot(path="Screenshots/PIM.png", full_page=True)
    assert page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    page.close()