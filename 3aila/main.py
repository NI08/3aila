from flask import Flask, render_template
from elts import UploadFileForm
from werkzeug.utils import secure_filename
import os

app = Flask("3aila")
app.config['SECRET_KEY'] = '12345678'
app.config['UPLOAD_FOLDER'] = 'static/files'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', "POST"])
def upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return "Le fichier est passé du bon coté de la force"
    return render_template('upload.html', form=form)

@app.route('/feed')
def feed():
    dossier = 'static/files'
    fichiers = [f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))]
    return render_template('feed.html', fichiers=fichiers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4200)
