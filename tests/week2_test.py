import pytest
from playwright.sync_api import sync_playwright, Browser, expect
from aux_func import login

def test_edit_my_info(browser: Browser):
    page = browser.new_page()
    login(page)  # login es una función definida en conftest.py
    page.click("text=My info")
    page.wait_for_load_state('networkidle')
    page.fill(selector="input[name='firstName']", value='giussepe')
    page.fill(selector="input[name='middleName']", value='Ernest')
    page.fill(selector="input[name='lastName']", value='Banquito')
    page.click('button[type=submit]')

    assert page.locator("input[name='firstName']").input_value() == 'giussepe'
    assert page.locator("input[name='middleName']").input_value() == 'Ernest'
    assert page.locator("input[name='lastName']").input_value() == 'Banquito'
    page.screenshot(path="Screenshots/Myinfo.png", full_page=True)
    page.close()



def test_add_emergency_contact(browser: Browser):
    page = browser.new_page()
    login(page) 
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmergencyContacts/empNumber/7")
    page.locator('button:text("Add")').first.click()
    #page.locator('button:text("Add")').click()
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(10000)
   

    page.locator("form").get_by_role("textbox").first.fill("Maria")
    page.locator("form").get_by_role("textbox").nth(1).fill("Brother")
    page.locator("form").get_by_role("textbox").nth(2).fill("-")
    page.locator("form").get_by_role("textbox").nth(3).fill("1175256723")
    page.locator("form").get_by_role("textbox").nth(4).fill("43255356")

    page.click('button[type=submit]')
    page.reload()
    page.wait_for_timeout(5000)
    last_row = page.get_by_role('table').filter(has_text="Relationship").get_by_role('row').last
    last_row_columns = last_row.get_by_role('cell').all()
    expect(last_row_columns[1]).to_have_text('Maria')
    expect(last_row_columns[2]).to_have_text('Brother')
    expect(last_row_columns[3]).to_have_text('-')
    expect(last_row_columns[4]).to_have_text('1175256723')
    expect(last_row_columns[5]).to_have_text('43255356')

    page.screenshot(path="Screenshots/EmergencyContact.png", full_page=True)
    page.close()
