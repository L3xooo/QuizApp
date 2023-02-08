import requests
import json
x = requests.get("https://the-trivia-api.com/api/questions")
# print(x.json())
for object in x.json():
    print(object.keys())
