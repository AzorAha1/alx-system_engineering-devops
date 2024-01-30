#!/usr/bin/python3
"""gather data from an api"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    nm_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    td_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response_name = requests.get(url=nm_url)
    response_todo = requests.get(url=td_url)
    data_name = response_name.json()
    data_todo = response_todo.json()
    empy_name = data_name['name']
    username = data_name['username']
    comptasksum = 0
    tasksum = 0
    for data in data_todo:
        if data['completed'] is True:
            comptasksum += 1
        tasksum += 1
    print(f'Employee {empy_name} is done with tasks({comptasksum}/{tasksum}):')
    for data in data_todo:
        if data['completed'] is True:
            print(f'\t {data["title"]}')
    formatted_data = {f'{employee_id}': []}
    for task in data_todo:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
            }
        formatted_data[f'{employee_id}'].append(task_data)
    with open(file=f'{employee_id}.json', mode='w') as jsonfile:
        json.dump(obj=formatted_data, fp=jsonfile)
