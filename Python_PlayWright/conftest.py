import pytest

BASE_URL = "https://opensource-demo.orangehrmlive.com"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL