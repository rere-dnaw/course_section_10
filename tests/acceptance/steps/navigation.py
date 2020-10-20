from behave import *
from selenium import webdriver
from tests.acceptance.models.home_page import HomePage
from tests.acceptance.models.blog_page import BlogPage
from tests.acceptance.models.new_post_page import NewPostPage

use_step_matcher('re')  # it's allow to receive arguments from the navigation.feature


@given('I am on the homepage.')
def step_impl(context):
    context.driver = webdriver.Firefox(
        executable_path=r'D:\Python\Course - Automation Testing Python\section10\geckodriver.exe')
    page = HomePage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page.')
def step_impl(context):
    """
    The function name can be the same because decorator will rename it.
    It's gonna relay on the step name.
    """
    expected_url = BlogPage(context.driver).url
    assert expected_url == context.driver.current_url


@given('I am on the blog page.')
def step_impl(context):
    context.driver = webdriver.Firefox(
        executable_path=r'D:\Python\Course - Automation Testing Python\section10\geckodriver.exe')
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@then('I am on the homepage.')
def step_impl(context):
    """
    The function name can be the same because decorator will rename it.
    It's gonna relay on the step name.
    """
    expected_url = HomePage(context.driver).url
    assert expected_url == context.driver.current_url


@Given('I am on the new post page.')
def step_impl(context):
    context.driver = webdriver.Firefox(
        executable_path=r'D:\Python\Course - Automation Testing Python\section10\geckodriver.exe')
    page = NewPostPage(context.driver)
    context.driver.get(page.url)

