import base64
import hashlib
import os, sys

from flask import Flask
from flask import request, make_response
from flask import render_template
from flask import redirect, url_for

app = Flask(__name__)

cur_dir = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = cur_dir + "/images"

# View 
@app.route('/', methods=['GET'])
def index():
    file1 = {'name': 'file1'} 
    file2 = {'name': 'file2'} 
    file3 = {'name': 'file3'} 
    files = [file1, file2, file3]
    return render_template('index.html', files=files)

@app.route('/delete/<string:filename>', methods=['POST', 'GET'])
def file_delete(filename):
    print ('file name: ' + filename)
    return redirect(url_for('index'))

@app.route('/upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'GET':
        return render_template('file_upload.html')
    elif request.method == 'POST':
        file1 = request.files['file1']
        file2 = request.files['file2']

        print (file1.filename)
        print (file2.filename)

        file1.save(app.config['UPLOAD_FOLDER'] + "/" +  file1.filename)
        file2.save(app.config['UPLOAD_FOLDER'] + "/" +  file2.filename)
        return 'OK'

       
if __name__ == '__main__':
    app.debug=True
    app.run(host='192.168.1.5')
