import pytest
from playwright.sync_api import sync_playwright

#esta funcion configura y proporciona una instancia de browser para utilizar en las pruebas
@pytest.fixture(scope="module") #Decorador de pytest que convierte la funcion browser en un 
#fixture (son funciones que se ejecutan antes de que comiencen tus test) Es como un BEFOREALL() en typescript
#pero tambien se puede configurar cambiando el scope para que sea antes de cada sesion, función, módulo etc.

def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()
