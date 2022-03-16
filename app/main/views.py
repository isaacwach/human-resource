from flask import render_template, redirect, request, url_for, abort
from . import main 

@main.route('/')
def index():
    return "Hello there"