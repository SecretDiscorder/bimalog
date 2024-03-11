import requests 
file_url = "https://github.com/SecretDiscorder/bimalog/releases/download/bimalog/manage.exe"

r = requests.get(file_url, stream = True) 


with open("manage.exe","wb") as exe: 
    for chunk in r.iter_content(chunk_size=1024): 
  
         # writing one chunk at a time to pdf file 
         if chunk: 
             exe.write(chunk) 
