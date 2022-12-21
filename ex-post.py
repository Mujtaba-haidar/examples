import requests


api_url = 'https://jsonplaceholder.typicode.com/todos'
todo = {"userID":1,"title":"let us play","complet":False}
respon = requests.post(api_url,json=todo)
print(respon.status_code)
print(respon.json())


