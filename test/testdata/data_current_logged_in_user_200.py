import requests
from testdata.api_enpoints import logged_in_user_endpoint
from testdata.parameters_and_payload import user_credential_200

response = requests.request("GET", logged_in_user_endpoint, params=user_credential_200)
response_body = response.json()
# print(response_body)