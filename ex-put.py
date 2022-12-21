import requests

api_url = 'https://jsonplaceholder.typicode.com/todos/10'
respon = requests.get(api_url)
print(respon.status_code)
print(respon.json())

todo = {"userID":1,"title":"wash car","complet":True}
respon = requests.put(api_url,json=todo)
print(respon.status_code)
print(respon.json())