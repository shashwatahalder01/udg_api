import allure
from testdata.data_signup_400 import response, response_body


@allure.step('Signup unsuccessful, status code validation')
def test_c002_01_status_code_is_400():
    assert response.status_code == 400


@allure.step("Signup unsuccessful, body not none validation")
def test_c002_02_response_body_not_none():
    assert response_body is not None


@allure.step("Signup unsuccessful, error message validation")
def test_c002_03_error_message():
    assert response_body['errors'][0]["message"] == "Email must be valid"


@allure.step("Signup unsuccessful, error field validation")
def test_c002_04_error_field():
    assert response_body['errors'][0]["field"] == "email"
