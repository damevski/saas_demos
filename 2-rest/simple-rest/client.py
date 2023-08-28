import requests

BASE_URL = 'http://127.0.0.1:5000'

def get_all_tasks():
    response = requests.get('http://127.0.0.1:5000/tasks')
    data = response.json()
    return data

def get_task(task_id):
    response = requests.get('http://127.0.0.1:5000/tasks/{task_id}')
    data = response.json()
    return data

def create_task(title):
    new_task = {"title": title}
    response = requests.post('http://127.0.0.1:5000/tasks', json=new_task)
    data = response.json()
    return data

if __name__ == '__main__':
    all_tasks = get_all_tasks()
    print("All Tasks:")
    print(all_tasks)

    task_id = 2
    specific_task = get_task(task_id)
    print(f"\nTask {task_id}:")
    print(specific_task)

    new_task_title = "new task"
    created_task = create_task(new_task_title)
    print(f"\nCreated Task:")
    print(created_task)
