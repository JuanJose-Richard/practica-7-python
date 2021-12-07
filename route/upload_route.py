from flask import request, jsonify
import server
from controller import car_controller
import os
#create
@server.app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(
            status ="failed"
        )
    file = request.files['file']

    if file.filename == '':
        return jsonify(
            status ="failed"
        )
    else:
        filename = file.filename
        file.save( os.path.join(server.app.config['UPLOAD_FOLDER'], filename) )   
        return jsonify(
            status ="success"
        )
