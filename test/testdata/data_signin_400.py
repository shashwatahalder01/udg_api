import requests
from testdata.headers import headers_post
from testdata.api_enpoints import sign_in_endpoint
from testdata.parameters_and_payload import payload_user_credential_400

response = requests.request("POST", sign_in_endpoint, headers=headers_post, data=payload_user_credential_400)
response_body = response.json()
# print(response_body)
