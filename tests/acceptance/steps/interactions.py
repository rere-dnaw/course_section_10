from behave import *

from tests.acceptance.locators.new_post_page import NewPostPageLocators
from tests.acceptance.models.base_page import BasePage
from tests.acceptance.models.new_post_page import NewPostPage

use_step_matcher('re')  # it's allow to receive arguments from the navigation.feature by using a regular expressions


@when('I press the link "(.*)"')
def step_impl(context, link_text):
    """
    The regular expression (.*) will put all char from between
    the "", into variable name.
    """
    page = BasePage(context.driver)
    links = page.navigation

    #found_links = [link for link in links if link.text == link_text]
    links.click()
    # if len(found_links) > 0:
    #     found_links[0].click()
    # else:
    #     raise RuntimeError()


@when('Enter "(.*)" into the "(.*)" field.')
def step_impl(context, content, field):
    return NewPostPage(context.driver).form_field(field).send_keys(content)


@when('Press submit button.')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_form.click()

