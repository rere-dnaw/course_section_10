from behave import *

from tests.acceptance.models.base_page import BasePage

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
