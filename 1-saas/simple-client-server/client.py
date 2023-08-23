import requests
url = 'http://127.0.0.1:5000/'


if __name__ == '__main__':
    r = requests.get(url)
    print(r.status_code)
    print(r.text)
