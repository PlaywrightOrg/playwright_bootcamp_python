from playwright.async_api import async_playwright

#hago una función aparte para e login para evitar la repetición de código
def login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill(selector="input[name='username']", value='Admin')
    page.fill(selector="input[name='password']", value='admin123')
    page.click('button[type=submit]')
    page.wait_for_load_state('networkidle')