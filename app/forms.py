import os
from flask import Flask, request, redirect, url_for,flash
from flask_wtf.file import FileField, FileRequired,FileAllowed
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    fileupload=FileField('image',validators=[FileRequired(),FileAllowed(['jpg', 'png',])])