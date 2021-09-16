import requests
from testdata.headers import headers_post
from testdata.api_enpoints import sign_in_endpoint
from testdata.parameters_and_payload import user_credential_200

response = requests.request("GET", sign_in_endpoint, headers=headers_post, params=user_credential_200)
response_body = response.json()
print(response_body)
