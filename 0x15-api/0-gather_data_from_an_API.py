#!/usr/bin/python3
"""gather data from an api"""
import requests, urllib.request
import json

url='https://jsonplaceholder.typicode.com/todos/1'
with urllib.request.urlopen(url=url) as request:
    data = json.load(request)
    employee_name = data['EMPLOYEE_NAME']
    number_of_done_tasks = data['NUMBER_OF_DONE_TASKS']
    total_number_of_tasks = data['TOTAL_NUMBER_OF_TASKS']
    task_title = data['TASK_TITLE']
    output = f'employee {employee_name}'
    print(output)