from pathlib import Path
from random import randint
from utils.excel_utils import read_single_col_open_file_once, get_row_count, write_single_col,get_row_count_specific_column, write_data
import uuid

user_file = Path(__file__).parent.parent / 'data/user_credentials.xlsx'
sheet_name = 'Sheet1'


def read_user_credential():
    max_row = get_row_count(user_file, sheet_name)
    user_credential = read_single_col_open_file_once(user_file, sheet_name, 2, max_row, 1)
    # print(user_credential)
    return user_credential


def new_user_generate():
    # new_site_name = f"user_{randint(0, 9999999999)}@mail.com"
    new_site_name = f"user_{uuid.uuid1()}@mail.com"
    return new_site_name


# def write_new_user_credential():
#     users = []
#     for i in range(10):
#         users.append(new_user_generate())
#     # print(*users,sep='\n')
#     write_single_col(user_file, sheet_name, len(users), 1, 2, users)

def write_new_valid_user_credential(user):
    writing_row = get_row_count(user_file, sheet_name) + 1
    # print(writing_row)
    write_data(user_file, sheet_name, writing_row, 1, user)



