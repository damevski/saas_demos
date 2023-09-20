import requests
import pytest
from requests.auth import HTTPDigestAuth

@pytest.fixture
def base_url():
    base_url = 'http://127.0.0.1:5000'
    return base_url

@pytest.fixture
def auth():
    auth = HTTPDigestAuth('rodney', 'go_rams')
    return auth

def test_not_found(base_url):
    url = base_url
    r = requests.get(url)
    assert(r.status_code == 404)

def test_get_tasks(base_url):
    url = base_url + '/tasks'
    r = requests.get(url)
    tasks = r.json()
    assert(len(tasks) > 0)

# usually a bad idea to change actual DB in a test
def test_add_task(base_url, auth):
    new_task = {'title': 'clean car'}
    r = requests.post('http://127.0.0.1:5000/tasks', json=new_task, auth=auth)
    assert(r.status_code == 201)
    #now check if the user is there
    url = base_url + '/tasks'
    r = requests.get(url)
    tasks = r.json()['tasks']
    assert(any(t['title'] == 'clean car' for t in tasks))

