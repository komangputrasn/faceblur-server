from flask import Flask, request
from image_blur import *

app = Flask(__name__, static_url_path='/static')

@app.route('/upload', methods=['POST'])
def upload_image():
    files = request.files.getlist('files')
    print('Files:', files)
    result = []
    for file in files:
        file.save(f'uploaded/{file.filename}')
        result.append(blur_children_faces(f'{file.filename}'))
    return result

if __name__ == '__main__':
    app.run()