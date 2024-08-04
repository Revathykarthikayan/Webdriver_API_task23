
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


class DragAndDrop:

    def __init__(self, url):
        self.url = url


        # Initialize WebDriver using ChromeDriverManager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.actions = ActionChains(self.driver)


    def navigate_to_webpage(self):

        self.driver.get(self.url)
        self.driver.maximize_window()


    def perform_drag_and_drop(self, frame_selector, draggable_xpath, droppable_xpath):
       
        try:

            # Switch to the frame containing the drag-and-drop elements

            frame = self.driver.find_element(By.CSS_SELECTOR, frame_selector)
            self.driver.switch_to.frame(frame)


            draggable_element = self.driver.find_element(By.XPATH, draggable_xpath)
            droppable_element = self.driver.find_element(By.XPATH, droppable_xpath)


            # Perform drag and drop

            self.actions.drag_and_drop(draggable_element, droppable_element).perform()
            time.sleep(5)


        except Exception as e:

            print(f"An error occurred: {e}")


        finally:

            self.quit()

    def quit(self):

        self.driver.quit()
        print("Browser closed")


if __name__ == "__main__":
    url = "https://jqueryui.com/droppable/"
    test = DragAndDrop(url)
    test.navigate_to_webpage()
    test.perform_drag_and_drop('.demo-frame', "//div[@id='draggable']", "//div[@id='droppable']")
    test.quit()