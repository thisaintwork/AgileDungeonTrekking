from behave import *
from characters.models import AdtCharacter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#use_step_matcher("re")


@given('Player navigates to Website "{page}"')
def step_impl(context, page):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)

    # Login to the Admin Panel
    context.selenium.get(f'{page}')
    assert (context.selenium.title == "Log-in")


@when('Player enters valid credentials')
def step_impl(context):
    # Fill Login Information
    username = context.selenium.find_element("id", "id_username")
    username.send_keys("adt_user1")
    password = context.selenium.find_element("id", "id_password")
    password.send_keys("adt_password123")

    # Locate login button and click on it
    context.selenium.find_element("xpath", '//input[@value="Log-in"]').click()
    assert (context.selenium.title == "Dashboard")


@when('Player creates a new character')
def step_impl(context):
    page = r"https://agiledungeontrekking.online/characters/"
    context.selenium.get(f'{page}')
    context.selenium.find_element("id", "btn_create_char").click()
    assert (context.selenium.title == "Create Character")


@then('Player can enter a name for the new character')
def step_impl(context):
    new_name = "Olaf Snowfellow"
    context.selenium.find_element("id", "id_name").sendKeys(new_name)
    name = context.selenium.find_element("id", "id_name")
    assert (name == new_name)


@then('The character has a name')
def step_impl(context):
    assert False

