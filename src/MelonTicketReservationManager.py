from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound


class MelonTicketReservationManager:
    def __init__(self, loger: any, ticket_url: str) -> None:
        self.__loger = loger
        self.__ticket_url = ticket_url
        self.__driver = webdriver.Chrome()
        return

    def __get_element_by_xpath(self, xpath: str) -> WebElement:
        self.__loger.log(f'Searching XPath: [ {xpath} ]')
        element = WebDriverWait(self.__driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        self.__loger.log(f'Element was successfully found: [ {element} ]')
        return element

    def __move_ticket_url(self) -> None:
        self.__loger.log(f'Moving Ticket Url: [ {self.__ticket_url} ]')
        self.__driver.get(self.__ticket_url)
        self.__driver.implicitly_wait(5)
        return

    def __click_reservation_button(self) -> None:
        xpath = '//*[@id="ticketReservation_Btn"]'
        element = self.__get_element_by_xpath(xpath)
        element.click()
        return

    def test_logic(self):
        self.__move_ticket_url()
        self.__click_reservation_button()
