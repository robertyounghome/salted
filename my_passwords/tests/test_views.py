# views (uses selenium)

# from django.test import TestCase
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from django.test import TestCase, LiveServerTestCase, TransactionTestCase
from django.contrib.auth.models import User
from my_passwords.models import Category 

# class TestSignup(LiveServerTestCase):

class TestSignup(TestCase):
    # fixtures = ['users.json']
    # @classmethod
    # def setUpTestData(cls):
    #     fixtures = ['users.json']

    def login(self):
        # Log the testuser in using the app
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        # self.driver.get('%s%s' %(self.live_server_url, '/accounts/login/'))
        self.driver.find_element_by_id('id_username').send_keys('testuser')
        self.driver.find_element_by_id('id_password').send_keys('opalescent')
        self.driver.find_element_by_id('submit').click()

    def setUp(self):
        super().setUp()
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Firefox(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome()
        self.login()

    # def test_login(self):
    #     self.login()
    #     self.assertIn("http://127.0.0.1:8000/", self.driver.current_url)

    # def test_index(self):
    #     # self.driver.get(self.live_server_url)
    #     # breakpoint()
    #     # Make sure we are logged in, otherwise error logging in 
    #     # self.assertIn("http://127.0.0.1:8000/", self.driver.current_url)
    #     # self.assertTrue(True)
    #     self.driver.implicitly_wait(5)
    #     self.assertIn(self.live_server_url, self.driver.current_url)

    def test_anything(self):
        # u = User.objects.get(id=1)
        # c = Category(name="Test Category", user = u)
        # c.save()
        breakpoint()
        self.assertTrue(True)


    def tearDown(self):
        super().tearDown()
        self.driver.quit

# if __name__ == '__main__':
#     unittest.main()