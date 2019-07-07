from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_reward(self):
        pass
        # 宣听说这里有个很酷的网站。可以激励自己努力。
        # 她访问网站的首页。
        # 她发现有个“写下你的目标”按钮。
        # 点击后，出现一个文本框，让她写下她的目标。
        # 点击输入后。弹出输入框，提示，你愿意为你的目标支付多少虚拟的美金。
        # 输入数值后。返回首页。
        # 首页出现一个“完成目标”的按钮。点击按钮，弹出对话框。你确认完成了目标了吗？点击是。
        # 获得虚拟的一百万美金。
        # 可以查看自己的虚拟美金。
        # 可以查看别人的虚拟美金。
        # 可以排名。
        # 可以邀请别人支付虚拟美金，助你完成目标。


    def test_can_start_a_list_for_one_user(self):
        # Edith hear there is a cool to-do list website.
        # She visits the home page of that website.
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # the page show up another frame, so that you can enter other to-do.
        # She input "Use peacock feathers to make a fly"
        # She was well-organized.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page update again, and shows that two to-do list.
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        
        # She was happy, and go to bed.

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith build a new to-do list.
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She noted that the to-do list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # now someone call Francis visit the webpage.

        ## we use a new browser session
        ## to make sure the data belongs Edith will not let out.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visit the home page.
        # that page did not show any of to-do list belongs Edith.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis enter a new to-do list
        # He has little to-do lists, didn't like Edith 
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis got his unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # this page did not show Edith's to-do list
        page_text = self.browser.find_element_by_id('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # both of two people were happy, and go to bed.


