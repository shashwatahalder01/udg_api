import json
from utils.user_credential_utils import new_user_generate, read_user_credential

new_user = new_user_generate()
# users = read_user_credential()
# new_user = users[0]

# parameter get request
user_credential_200 = {
    "email": "user@mail.com",
    "password": "Asdfgh123!"
}

user_credential_401 = {
    'email': '',
    'password': 'Asdfgh123!'
}

# payload post request
payload_user_credential_201_signin = json.dumps({
    "email": "user@mail.com",
    "password": "ndsfGjJdf4325sg"
})

payload_user_credential_201_signup = json.dumps({
    "email": new_user,
    "password": "Asdfgh123!"
})

payload_user_credential_400 = json.dumps({
    "email": "",
    "password": "Asdfgh123!"
})
