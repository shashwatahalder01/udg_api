import json
from utils.user_credential_utils import new_user_generate

new_user = new_user_generate()

# parameter get request
user_credential_200 = {
    "email": "user@mail.com",
    "password": "Asdfgh123!"
}

user_credential_401 = {
    'email': '',
    'password': 'Asdfgh123!'
}

# api payloads

payload_with_only_email = json.dumps({
    "email": "user@mail.com",
    "password": ""
})

payload_with_only_password = json.dumps({
    "email": "",
    "password": "Asdfgh123!"
})

payload_without_email_password = json.dumps({
    "email": "",
    "password": ""
})

payload_with_fixed_valid_email_password = json.dumps({
    "email": "user@mail.com",
    "password": "ndsfGjJdf4325sg"
})

payload_with_new_email_password = json.dumps({
    "email": new_user,
    "password": "Asdfgh123!"
})
