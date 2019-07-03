from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith hear there is a cool to-do list website.
        # She visits the home page of that website.
        self.browser.get('http://localhost:8000')

        # She noted that the title and the head of the website both include the item "To-Do"
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # the app require her enter a to-do list item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she input "Buy peacock feathers" in a form.
        # Edith loves fishing.
        inputbox.send_keys('Buy peacock feathers')

        # The webpage update after she hit the Key Enter.
        # The table shows"1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # the page show up another frame, so that you can enter other to-do.
        # She input "Use peacock feathers to make a fly"
        # She was well-organized.
        self.fail('Finish the text!')

        # The page update again, and shows that two to-do list.

        # Edith want to know if the website have keeped her to-do list.
        # She saw the web give a unique URL for her.
        # And the page have some help text.

        # She visited that URL, and found that her to-do list still there.
        # She was happy and go to bed.
if __name__ == '__main__':
    unittest.main(warnings='ignore')