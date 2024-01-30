#!/usr/bin/python3
"""gather data from an api"""
import requests, urllib.request

url='https://jsonplaceholder.typicode.com/todos/$2'
with urllib.request.urlopen(url=url) as request:
    print(request)