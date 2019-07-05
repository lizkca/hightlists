from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

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
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # the page show up another frame, so that you can enter other to-do.
        # She input "Use peacock feathers to make a fly"
        # She was well-organized.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page update again, and shows that two to-do list.
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith want to know if the website have keeped her to-do list.
        # She saw the web give a unique URL for her.
        # And the page have some help text.
        self.fail('Finish the text!')

        # She visited that URL, and found that her to-do list still there.
        # She was happy and go to bed.
if __name__ == '__main__':
    unittest.main(warnings='ignore')