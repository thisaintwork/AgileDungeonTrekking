from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#use_step_matcher("re")
import random_name_generator as rname


new_name = rname.generate(limit=1)[0]

@given('Player navigates to Website "{page}"')
def step_impl(context, page):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)

    # Login to the Admin Panel
    context.selenium.get(f'{page}')
    assert (context.selenium.title == "Log-in")


@when('Player enters username "{}" and password "{}" as valid credentials')
def step_impl(context, username, password):
    # Fill Login Information
    id_username = context.selenium.find_element(By.ID, "id_username")
    id_username.send_keys(username)
    id_password = context.selenium.find_element(By.ID, "id_password")
    id_password.send_keys(password)

    # Locate login button and click on it
    context.selenium.find_element(By.XPATH, '//input[@value="Log-in"]').click()
    assert (context.selenium.title == "Dashboard")


@when('Player creates a new character')
def step_impl(context):
    page = r"https://agiledungeontrekking.online/characters/"
    context.selenium.get(f'{page}')
    context.selenium.find_element(By.ID, "btn_create_char").click()
    context.selenium.find_element(By.ID, "id_image").send_keys('static/img/characters/char1.png')
    assert (context.selenium.title == "Create Character")


@then('Player can enter a name for the new character')
def step_impl(context):
    #name_fld = context.selenium.find_element(By.XPATH, '//input[@type="text"]')
    name_fld = context.selenium.find_element(By.ID, "id_name")
    name_fld.send_keys(new_name)
    valid_name = name_fld.get_attribute("value")
    assert (valid_name == new_name)
    context.selenium.find_element(By.ID, "id_save").submit()


@then('The character has a name')
def step_impl(context):
    print(context.selenium.title)
    assert ("Manage Characters" in context.selenium.title)
    chars = context.selenium.find_elements(By.TAG_NAME, "a")
    # find the new character
    for c in chars:
        found = (c.text == new_name)
    assert found

