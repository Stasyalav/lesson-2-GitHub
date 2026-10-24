import requests
r = requests.get("https://money.robolatoriya.com/api/currency/dashboard")
print(r.status_code)
