import requests

url = "http://0.0.0.0:8000/evaluate"
data = {
    "feature": "centerline-artifacts"
}
response = requests.post(url, json=data)
print(response.text)