from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import unittest

MAX_WAIT = 5


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_poll_site(self):
        # Edith has heard about a cool new online poll site. She goes
        # to check out its homepage
        #self.browser.get(self.live_server_url)
        self.browser.get("http://localhost:8000/polls/")

        # She notices the page title and header mention to-do lists
        self.assertEqual('Polls site', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn('Hello, world', header_text)





#OUTANDTODELETE    def wait_for_row_in_list_table(self, row_text):
#OUTANDTODELETE        start_time = time.time()
#OUTANDTODELETE        while True:
#OUTANDTODELETE            try:
#OUTANDTODELETE                table = self.browser.find_element(By.ID, "id_list_table")  
#OUTANDTODELETE                rows = table.find_elements(By.TAG_NAME, "tr")
#OUTANDTODELETE                self.assertIn(row_text, [row.text for row in rows])
#OUTANDTODELETE                return
#OUTANDTODELETE            except (AssertionError, WebDriverException):
#OUTANDTODELETE                if time.time() - start_time > MAX_WAIT:
#OUTANDTODELETE                    raise
#OUTANDTODELETE                time.sleep(0.5)
#OUTANDTODELETE
#OUTANDTODELETE    def test_can_start_a_todo_list(self):
#OUTANDTODELETE        # Edith has heard about a cool new online to-do app. She goes
#OUTANDTODELETE        # to check out its homepage
#OUTANDTODELETE        self.browser.get(self.live_server_url)
#OUTANDTODELETE
#OUTANDTODELETE        # She notices the page title and header mention to-do lists
#OUTANDTODELETE        self.assertIn('To-Do', self.browser.title)
#OUTANDTODELETE        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
#OUTANDTODELETE        self.assertIn('To-Do', header_text)
#OUTANDTODELETE
#OUTANDTODELETE        # She is invited to enter a to-do item straight away
#OUTANDTODELETE        inputbox = self.browser.find_element(By.ID, "id_new_item")
#OUTANDTODELETE        self.assertEqual(
#OUTANDTODELETE            inputbox.get_attribute('placeholder'),
#OUTANDTODELETE            'Enter a to-do item'
#OUTANDTODELETE        )
#OUTANDTODELETE
#OUTANDTODELETE        # She types "Buy peacock feathers" into a text box
#OUTANDTODELETE        # (Edith's hobby is tying fly-fishing lures)
#OUTANDTODELETE
#OUTANDTODELETE        inputbox.send_keys("Buy peacock feathers")
#OUTANDTODELETE
#OUTANDTODELETE        # When she hits enter, the page updates, and now the page lists
#OUTANDTODELETE        # "1: Buy peacock feathers" as an item in a to-do list
#OUTANDTODELETE        inputbox.send_keys(Keys.ENTER)
#OUTANDTODELETE        self.wait_for_row_in_list_table("1: Buy peacock feathers")
#OUTANDTODELETE
#OUTANDTODELETE        # There is still a text box inviting her to add another item. She
#OUTANDTODELETE        # enters "Use peacock feathers to make a fly" (Edith is very
#OUTANDTODELETE        # methodical)
#OUTANDTODELETE        inputbox = self.browser.find_element(By.ID, "id_new_item")
#OUTANDTODELETE        inputbox.send_keys('Use peacock feathers to make a fly')
#OUTANDTODELETE        inputbox.send_keys(Keys.ENTER)
#OUTANDTODELETE
#OUTANDTODELETE        # The page updates again, and now shows both items on her list
#OUTANDTODELETE        self.wait_for_row_in_list_table("1: Buy peacock feathers")
#OUTANDTODELETE        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")
#OUTANDTODELETE
#OUTANDTODELETE        # Satisfied, she goes back to sleep
#OUTANDTODELETE
#OUTANDTODELETE    def test_multiple_users_can_start_lists_at_different_urls(self):
#OUTANDTODELETE        # Edith starts a new to-do list
#OUTANDTODELETE        self.browser.get(self.live_server_url)
#OUTANDTODELETE        inputbox = self.browser.find_element(By.ID, "id_new_item")
#OUTANDTODELETE        inputbox.send_keys("Buy peacock feathers")
#OUTANDTODELETE        inputbox.send_keys(Keys.ENTER)
#OUTANDTODELETE        self.wait_for_row_in_list_table("1: Buy peacock feathers")  
#OUTANDTODELETE
#OUTANDTODELETE        # She notices that her list has a unique URL
#OUTANDTODELETE        edith_list_url = self.browser.current_url
#OUTANDTODELETE        self.assertRegex(edith_list_url, '/lists/.+')
#OUTANDTODELETE
#OUTANDTODELETE        # Now a new user, Francis, comes along to the site.
#OUTANDTODELETE
#OUTANDTODELETE        ## We delete all the browser cookies
#OUTANDTODELETE        ## as a way of simulating a brand new user session
#OUTANDTODELETE        self.browser.delete_all_cookies()
#OUTANDTODELETE
#OUTANDTODELETE        # Francis visits the home page. There is no sign of Edith's list
#OUTANDTODELETE        self.browser.get(self.live_server_url)
#OUTANDTODELETE        page_text = self.browser.find_element(By.TAG_NAME, "body").text
#OUTANDTODELETE        self.assertNotIn("Buy peacock feathers", page_text)
#OUTANDTODELETE        self.assertNotIn("make a fly", page_text)
#OUTANDTODELETE
#OUTANDTODELETE        # Francis starts a new list by entering a new item.
#OUTANDTODELETE        # He is less interesting than Edith
#OUTANDTODELETE        inputbox = self.browser.find_element(By.ID, "id_new_item")
#OUTANDTODELETE        inputbox.send_keys("Buy milk")
#OUTANDTODELETE        inputbox.send_keys(Keys.ENTER)  
#OUTANDTODELETE        self.wait_for_row_in_list_table("1: Buy milk")
#OUTANDTODELETE
#OUTANDTODELETE        # Francis gets his own unique URL
#OUTANDTODELETE        francis_list_url = self.browser.current_url
#OUTANDTODELETE        self.assertRegex(francis_list_url, '/lists/.+')
#OUTANDTODELETE        self.assertNotEqual(francis_list_url, edith_list_url)
#OUTANDTODELETE
#OUTANDTODELETE        # Again, there is no trace of Edith's list
#OUTANDTODELETE        page_text = self.browser.find_element(By.TAG_NAME, "body").text
#OUTANDTODELETE        self.assertNotIn("Buy peacock feathers", page_text)
#OUTANDTODELETE        self.assertIn("Buy milk", page_text)
#OUTANDTODELETE
#OUTANDTODELETE        # Satisfied, they both go back to sleep


#if __name__ == '__main__':
#    unittest.main()