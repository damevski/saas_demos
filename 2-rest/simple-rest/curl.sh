curl -X GET http://127.0.0.1:5000/tasks
curl -X GET http://127.0.0.1:5000/tasks/2
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Task"}' http://127.0.0.1:5000/tasks

