from flask import Flask

app = Flask(__name__)

FILE_FOLDER = r'D:/material cursos/cursosCisco/cursoPython\dev/python/projects/env2/flask/uploads'
app.config['UPLOAD_FOLDER']= FILE_FOLDER
@app.route('/')
def index():
    return "Mi primera web con FLASK"