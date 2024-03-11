import requests 
file_url = "https://github.com/SecretDiscorder/bimalog/releases/download/bimalog/manage.exe"

r = requests.get(file_url, stream = True) 

