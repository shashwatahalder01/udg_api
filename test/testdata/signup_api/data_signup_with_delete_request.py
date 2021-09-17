import requests
from testdata.headers import headers_post
from testdata.api_enpoints import signup_endpoint
from testdata.parameters_and_payload import payload_with_new_email_password

response = requests.request("DELETE", signup_endpoint, headers=headers_post, data=payload_with_new_email_password)
# response = requests.request("DELETE", signup_endpoint, headers=headers_post)
response_body = response.json()
# print(response_body)
