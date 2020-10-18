from selenium.webdriver.common.by import By


class BlogPageLocators:
    TITLE = By.TAG_NAME, "h1"
    HOME_LINK = By.ID, "home-link"
    CREATE_POST_LINK = By.ID, "add-post-link"
    BLOG_URL = "/blog"
    POSTS_SECTION = By.ID, "posts"
    POST = By.CLASS_NAME, "post-link"
