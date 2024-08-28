from playwright.sync_api import sync_playwright, expect

import unittest

with sync_playwright() as playwright:

    #Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)

    #Create a new page
    page = browser.new_page()

    #Visit the playwright website
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #Log in
    page.fill(selector="input[name='username']", value = 'Admin')
    page.fill(selector="input[name='password']", value = 'admin123')
    page.click('button[type=submit]')
   
    #Assertion Log in
   #dashboard_text = page.text_content(".oxd-text.oxd-text--h6")
    #assert dashboard_text == "Dashboard"

    #Go to "My info"
    page.click("text = My info")
    #page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7")
    
    #Assertion de "My Info"
    #Myinfo_text = page.text_content("oxd-text oxd-text--h6")
    #assert Myinfo_text == "PIM"

    #Update info
    page.fill(selector="input[name='firstName']", value = 'giussepe')
    page.fill(selector="input[name='middleName']", value = 'Ernest')
    page.fill(selector="input[name='lastName']", value = 'Banquito')
    page.click('button[type=submit]')

    #Assertion de info actualizada
    #fn_text = page.text_content("oxd-input oxd-input--active orangehrm-firstname")
    #assert fn_text == "giussepe"
    expect(page.input_value('firstName')).toContainText('giussepe')
    expect(page.input_value('middleName')).toContainText('Ernest')
    expect(page.input_value('lastName')).toContainText('Banquito')

    #Screenshot
    page.screenshot(path="Screenshots/Myinfo.png", full_page=True)

    #Go to "Emergency Contacts"
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmergencyContacts/empNumber/7")

    #Button Add

    page.locator('button:text("Add")').click()

    #Completando datos del contacto de emergencia
    page.fill(selector="input[name='Name']", value = 'Arnaldo')
    page.fill(selector="input[name='Relationship']", value = 'Brother')
    page.fill(selector="input[name='HomeTelephone']", value = '-')
    page.fill(selector="input[name='Mobile']", value = '1175256723')
    page.fill(selector="input[name='workTelephone']", value = '43255356')
    page.click('button[type=submit]')
    
    #Assertions de EmergencyContact
    expect(page.locator).toContainText('Arnaldo')
    expect(page.locator).toContainText('Brother')
    expect(page.locator).toContainText('-')
    expect(page.locator).toContainText('1175256723')
    expect(page.locator).toContainText('43255356')

    #Screenshot
    page.screenshot(path="Screenshots/EmergencyContact.png", full_page=True)