#!/usr/bin/python3
"""gather data from an api"""
import requests, urllib.request
import json, sys

employee_id = int(sys.argv[1])
url=f'https://jsonplaceholder.typicode.com/todos/{employee_id}'
with urllib.request.urlopen(url=url) as request:
    data = json.load(request)
    employee_name = data['EMPLOYEE_NAME']
    number_of_done_tasks = data['NUMBER_OF_DONE_TASKS']
    total_number_of_tasks = data['TOTAL_NUMBER_OF_TASKS']
    task_title = data['title']
    output = f'employee {task_title}'
    print(output)