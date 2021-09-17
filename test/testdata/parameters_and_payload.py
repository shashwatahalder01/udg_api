import json
from utils.user_credential_utils import new_user_generate

new_user = new_user_generate()

# parameter get request
params_with_fixed_email_password = {
    "email": "user@mail.com",
    "password": "Asdfgh123!"
}

params_with_only_password = {
    'email': '',
    'password': 'Asdfgh123!'
}

# api payloads

payload_with_only_email = json.dumps({
    "email": "user@mail.com",
    # "password": ""
})

payload_with_only_password = json.dumps({
    # "email": "",
    "password": "Asdfgh123!"
})

payload_without_email_password = json.dumps({
    # "email": "",
    # "password": ""
})

payload_with_fixed_valid_email_password = json.dumps({
    "email": "user@mail.com",
    "password": "ndsfGjJdf4325sg"
})

payload_with_new_email_password = json.dumps({
    "email": new_user,
    "password": "Asdfgh123!"
})
