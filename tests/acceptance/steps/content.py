from behave import *

from tests.acceptance.models.base_page import BasePage
from tests.acceptance.models.blog_page import BlogPage

use_step_matcher('re')  # it's allow to receive arguments from the navigation.feature


@then('The title is present on the page.')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


#  @then('The title is "(.*)".')
@step('The title is "(.*)".')  # if we want to use this step not only as "then", use "step" instead
def step_impl(context, expect_title):
    tag_name = BasePage(context.driver)
    assert tag_name.title.text == expect_title


@then("The post section is present on the page")
def step_imp(context):
    assert BlogPage(context.driver).posts_section.is_displayed()

@then('The new post title is "(.*)"')
def step_impl(context, text):
    page = BlogPage(context.driver).post

    test = 2