from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('I click the "{button_id}" button')
def step_impl(context, button_id):
    """ Click a button element by its ID """
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, button_id))
    )
    button.click()

@then('I should see "{text}" in the results')
def step_impl(context, text):
    """ Verify that specific text appears on the page """
    found = WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), text)
    )
    assert found is True, f"Text '{text}' not found in the results"

@then('I should not see "{text}" in the results')
def step_impl(context, text):
    """ Verify that specific text does not appear on the page """
    element = context.driver.find_element(By.TAG_NAME, "body")
    assert text not in element.text, f"Text '{text}' was found, but it should not be"

@then('I should see the message "{message}"')
def step_impl(context, message):
    """ Verify that a specific system message appears """
    message_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash-message"))
    )
    assert message in message_element.text, f"Expected '{message}', but found: '{message_element.text}'"

