from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import PyPDF2 as pdf
app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        #f.save(secure_filename(f.filename))
        pdf_reader = pdf.PdfFileReader(f)
        print(pdf_reader.getIsEncrypted())
        print(pdf_reader.getNumPages())
        'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)