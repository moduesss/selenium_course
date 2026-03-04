import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def register_user(self, url):
        browser = webdriver.Chrome()
        try:
            browser.get(url)

            browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
            browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
            browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("ivan.petrov@example.com")

            browser.find_element(By.CSS_SELECTOR, "button.btn").click()

            welcome_text = browser.find_element(By.TAG_NAME, "h1").text
            self.assertEqual(
                "Congratulations! You have successfully registered!",
                welcome_text,
            )
        finally:
            browser.quit()

    def test_registration1(self):
        self.register_user("http://suninjuly.github.io/registration1.html")

    def test_registration2(self):
        self.register_user("http://suninjuly.github.io/registration2.html")


if __name__ == "__main__":
    unittest.main()
