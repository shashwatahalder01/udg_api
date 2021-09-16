import allure
from testdata.data_signin_200 import response, response_body


@allure.step('Signin successful, status code validation')
def test_c003_01_status_code_is_200():
    assert response.status_code == 200


@allure.step("Signin successful, body not none validation")
def test_c003_02_response_body_not_none():
    assert response_body is not None


@allure.step("Signin successful, body field token validation")
def test_c003_03_body_field_email():
    assert 'email' in response_body


@allure.step("Signin successful, body field token validation")
def test_c003_04_body_field_token():
    assert 'token' in response_body
