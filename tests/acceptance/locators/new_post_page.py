from selenium.webdriver.common.by import By


class NewPostPageLocators:
    POST_FORM_ID = By.ID, "post-form"
    TITLE_ID = By.ID, "title"
    CONTENT_ID = By.ID, "content"
    SUBMIT_ID = By.ID, "create-post"
    NEW_POST_URL = "/post"
