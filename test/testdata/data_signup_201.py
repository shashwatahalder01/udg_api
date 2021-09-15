import requests
from testdata.headers import headers_post
from testdata.api_enpoints import signup_endpoint
from testdata.parameters_and_payload import *
from utils.user_credential_utils import write_new_valid_user_credential
# import json

response = requests.request("POST", signup_endpoint, headers=headers_post, data=payload_user_credential_201_signup)
response_body = response.json()
# print(response_body)

# Write valid user to excel
if response.status_code == 201:
    # print(new_user)
    write_new_valid_user_credential(new_user)

# response = ''
# response_body = ''
# count = 0
# while True:
#
#     if count > 9:
#         break
#     count = count + 1
#     payload_user_credential_201_signup = json.dumps({
#         "email": new_user_generate(),
#         "password": "Asdfgh123!"
#     })
#     response = requests.request("POST", signup_endpoint, headers=headers_post, data=payload_user_credential_201_signup)
#     response_body = response.json()
#     if response.status_code == 201:
#         break
# print(response_body)
