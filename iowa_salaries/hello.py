# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 11:03:51 2022

@author: Dustin
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"