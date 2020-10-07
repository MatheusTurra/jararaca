from flask import Flask, render_template, request

from ocr_core import ocr_core

UPLOAD_FOLDER = '/static/images/'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', msg='Nenhum arquivo enviado')
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', msg='Nenhum arquivo selecionado')
        if file and allowed_file(file.filename):
            extracted_text = ocr_core(file)
            # print(UPLOAD_FOLDER + file.filename)
            return render_template('upload.html',
                                   msg='Processada com sucesso',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run()
