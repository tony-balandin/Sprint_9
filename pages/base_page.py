from __future__ import annotations

from pathlib import Path

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def find(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_present(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple[str, str]) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            element,
        )
        try:
            element.click()
        except Exception:
            ActionChains(self.driver).move_to_element(element).click().perform()

    def fill(self, locator: tuple[str, str], value: str) -> None:
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def upload_file(self, locator: tuple[str, str], file_path: Path) -> None:
        element = self.find_present(locator)
        element.send_keys(str(file_path.resolve()))

    def is_visible(self, locator: tuple[str, str]) -> bool:
        try:
            self.find(locator)
            return True
        except TimeoutException:
            return False

    def wait_for_url_to_be(self, value: str) -> bool:
        return self.wait.until(EC.url_to_be(value))

    def wait_for_url_contains(self, value: str) -> bool:
        return self.wait.until(EC.url_contains(value))

    def current_url(self) -> str:
        return self.driver.current_url
