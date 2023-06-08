Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... img = <'replace-with-path-to-image'>
... api_user_token = <'replace-with-your-api-user-token'>
... headers = {'Authorization': 'Bearer ' + api_user_token}
... 
... # Food Type Detection
... url = 'https://api.logmeal.es/v2/image/recognition/type'
... resp = requests.post(url,files={'image': open(img, 'rb')}, headers=headers)
... print(resp.json()) # display json response
SyntaxError: multiple statements found while compiling a single statement
