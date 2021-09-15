import requests
from testdata.headers import headers_post
from testdata.api_enpoints import signup_endpoint
from testdata.parameters_and_payload import *
# import json

response = requests.request("POST", signup_endpoint, headers=headers_post, data=payload_user_credential_201_signup)
response_body = response.json()
print(response_body)

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
