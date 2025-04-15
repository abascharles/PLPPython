import requests

response = requests.get('https://api.github.com/')
print(response.status_code)  # Print the status code of the response 