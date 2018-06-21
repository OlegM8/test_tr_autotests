from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)


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