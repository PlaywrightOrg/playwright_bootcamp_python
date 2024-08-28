from playwright.sync_api import sync_playwright

#.\Week1\Scripts\activate

with sync_playwright() as playwright:
    #Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    #Create a new page
    page = browser.new_page()
    #Visit the playwright website
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #Take Screenshot
    page.screenshot(path="Screenshots/Loginpage.png", full_page=True)

     #Log in
    page.fill(selector="input[name='username']", value = 'Admin')
    page.fill(selector="input[name='password']", value = 'admin123')
    page.click('button[type=submit]')

    #Go Directory page
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory")
    #Take Screenshot

    page.screenshot(path="Screenshots/Directory.png", full_page=True)
    #Go PIM page

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

    #Take Screenshot
    page.screenshot(path="Screenshots/PIM.png", full_page=True)

    browser.close()