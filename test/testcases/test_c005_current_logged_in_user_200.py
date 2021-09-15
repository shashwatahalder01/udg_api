import allure
from testdata.data_current_logged_in_user_200 import response, response_body


@allure.step('Logged_in user details, status code validation')
def test_c005_01_status_code_is_200():
    assert response.status_code == 200


@allure.step("Logged_in user details, body not none validation")
def test_c005_02_response_body_not_none():
    assert response_body is not None
