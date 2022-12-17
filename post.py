import requests

name = input("Input student name: ")
student = {"name" : name}
headers = {"Content type" : "application/json"}

response = requests.post("https://reqres.in/api/users", json = student , headers = headers)

print(response.content)
print(response.headers)
print(response.status_code)
