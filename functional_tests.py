from selenium import webdriver
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
        self.fail('Finish the test!')

        # the app require her enter a to-do list item.

        # she input "Buy peacock feathers" in a form.
        # Edith loves fishing.

        # The webpage update after she hit the Key Enter.
        # The table shows"1: Buy peacock feathers"

        # the page show up another frame, so that you can enter other to-do.
        # She input "Use peacock feathers to make a fly"
        # She was well-organized.

        # The page update again, and shows that two to-do list.

        # Edith want to know if the website have keeped her to-do list.
        # She saw the web give a unique URL for her.
        # And the page have some help text.

        # She visited that URL, and found that her to-do list still there.
        # She was happy and go to bed.
if __name__ == '__main__':
    unittest.main(warnings='ignore')