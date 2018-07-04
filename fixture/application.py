from selenium import webdriver
from fixture.session import SessionHelper
from fixture.calculator import CalcHelper


capabilities = {
    "browserName": "firefox",
    "version": "58.0",
    "enableVNC": True
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities,
    )


class Application:

    def __init__(self):
        self.wd = driver
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.calculator = CalcHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get("https://olegtesttr.000webhostapp.com/")

    def destroy(self):
        self.wd.quit()