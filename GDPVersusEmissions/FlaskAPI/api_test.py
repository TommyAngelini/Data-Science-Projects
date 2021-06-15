# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:59:59 2021

@author: tomas
"""

import requests


data = [1500.0, 0.0]

URL = 'http://127.0.0.1:5000/predict'
headers = {'Content-Type': 'application/json'}
data = {"input": data}

r = requests.get(URL, headers=headers, json = data)
r.json()