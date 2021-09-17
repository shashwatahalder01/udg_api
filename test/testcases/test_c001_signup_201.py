# import allure
# from testdata.data_signup_201 import response, response_body
#
#
# @allure.step('Signup successful, status code validation')
# def test_c001_01_status_code_is_201():
#     assert response.status_code == 201
#
#
# @allure.step("Signup successful, body not none validation")
# def test_c001_02_response_body_not_none():
#     assert response_body is not None
#
#
# @allure.step("Signin successful, body field token validation")
# def test_c001_03_body_field_email():
#     assert 'email' in response_body
#
#
# @allure.step("Signin successful, body field token validation")
# def test_c001_04_body_field_token():
#     assert 'token' in response_body
