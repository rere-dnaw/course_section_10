from selenium.webdriver.common.by import By

from tests.acceptance.models.base_page import BasePage
from tests.acceptance.locators.new_post_page import NewPostPageLocators

import selenium


class NewPostPage(BasePage):
    @property
    def url(self):
        return super(NewPostPage, self).url + NewPostPageLocators.NEW_POST_URL

    @property
    def form(self):
        return self.driver.find_elements(*NewPostPageLocators.POST_FORM_ID)

    @property
    def submit_form(self):
        return self.driver.find_elements(*NewPostPageLocators.SUBMIT_ID)[0]

    def form_field(self, name):
        return self.form[0].find_element(By.NAME, name)


