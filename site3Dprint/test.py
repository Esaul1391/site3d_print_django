import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase


class BasicInstallTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn("Сайт 3d печати", self.browser.title)