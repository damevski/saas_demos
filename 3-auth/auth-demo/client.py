import requests
from requests.auth import HTTPDigestAuth

BASE_URL = "http://127.0.0.1:5000"
USERNAME = "rodney"
PASSWORD = "go_rams"

def start_stopwatch():
    response = requests.get(f"{BASE_URL}/start", 
                            auth=HTTPDigestAuth(USERNAME, PASSWORD))
    print(response.text)

def get_elapsed_time():
    r = requests.get(f"{BASE_URL}/stop", 
                     auth=HTTPDigestAuth(USERNAME, PASSWORD))
    data = r.json()
    elapsed_time = data["elapsed_time"]
    print(f"Elapsed Time: {elapsed_time} seconds")

if __name__ == "__main__":
    start_stopwatch()
    input("Press Enter to get elapsed time...")
    get_elapsed_time()
