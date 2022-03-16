from flask import render_template, redirect, request, url_for, abort
from . import main 
from flask_login import login_required, current_user
from .. import db,photos
from ..models import User


@main.route('/')
def index():
    return "Hello there"