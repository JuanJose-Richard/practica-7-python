from flask import request, jsonify, send_file

import server
from controller import car_controller
#create
@server.app.route('/download/<filename>')
def download_file():
    file_path = server.app.config['UPLOAD_FOLDER']+filename
    return send_file(file_path, as_attachment=true)
     


