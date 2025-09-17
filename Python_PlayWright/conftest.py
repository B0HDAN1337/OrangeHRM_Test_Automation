import pytest

BASE_URL = "https://opensource-demo.orangehrmlive.com"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture()
def logged_in_user(browser):
    context = browser.new_context(storage_state="storage_state.json")
    page = context.new_page()
    yield page
    context.close()