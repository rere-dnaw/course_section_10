from tests.acceptance.models.base_page import BasePage
from tests.acceptance.locators.blog_page import BlogPageLocators


class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + BlogPageLocators.BLOG_URL

    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def post(self):
        """
        Return all the posts
        """
        return self.driver.find_element(*BlogPageLocators.POST)

    @property
    def post_link(self):
        return self.driver.find_element(*BlogPageLocators.CREATE_POST_LINK)

    @property
    def home_link(self):
        return self.driver.find_element(*BlogPageLocators.HOME_LINK)