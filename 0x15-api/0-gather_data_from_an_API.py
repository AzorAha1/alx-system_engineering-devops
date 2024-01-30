#!/usr/bin/python3
"""gather data from an api"""
import requests
import sys

if __name__ == "__main":
    employee_id = int(sys.argv[1])
    name_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response_name = requests.get(url=name_url)
    response_todo = requests.get(url=todos_url)
    data_name = response_name.json()
    data_todo = response_todo.json()
    employee_name = data_name['name']
    completed_task_sum = 0
    all_task_sum = 0
    for data in data_todo:
        if data['completed'] is True:
            completed_task_sum += 1
        all_task_sum += 1
    print(f'Employee {employee_name}\
            is done tasks({completed_task_sum}/{all_task_sum}):')
    for data in data_todo:
        print(f'\t {data["title"]}')
