import hashlib

import requests

url = 'https://api.pwnedpasswords.com/range/'


def request_api_data(query_char):
    res = requests.get(f'{url}{query_char}')
    if res.status_code != 200:
        raise Exception(f'Something went wrong {res.status_code}, {res.content.decode("utf-8")}')
    return res


def get_password_leaks_count(hashes, has_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines() if has_to_check in line)
    co = 0
    for hash, count in hashes:
        co += int(count)
    return co


def pwned_api_check(password):
    # Encode to hash
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # Split hash by first 5 chars and the rest
    first_5_char, tail = sha1pwd[:5], sha1pwd[5:]
    # Check leaks by first 5 chars
    response = request_api_data(first_5_char)
    # Find count of leaks by the rest of the hash
    leaks_count = get_password_leaks_count(response, tail)
    print(f'There are {leaks_count} matches for the password ({password})')
    return leaks_count


print('Please define passwords you wanna check (empty password to finish): ')
passwords_to_check = []
while True:
    text = input(' - ')
    if not text:
        break
    passwords_to_check.append(text)

for password in passwords_to_check:
    pwned_api_check(password)
