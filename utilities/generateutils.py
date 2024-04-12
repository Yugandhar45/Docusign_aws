import logging as logger
import random
import string


def generate_string(company_prefix=None):
    logger.info('Generate random string')
    if not company_prefix:
        company_prefix = 'Pharmateksol'

    random_string_length = 5
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_string_length))
    company_name = company_prefix + ' ' + random_string
    random_info = {'company_name': company_name}
    return random_info


def generate_random_userName(user_name_prefix=None):
    logger.info('Generate random user name')
    if not user_name_prefix:
        user_name_prefix = 'testuser'
    random_string_length = 5
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_string_length))
    full_name = user_name_prefix + ' ' + random_string
    random_full_name = {'full_name': full_name}
    print(full_name)
    return random_full_name
