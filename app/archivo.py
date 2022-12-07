from flask import Blueprint,request, redirect ,flash,url_for,send_from_directory, render_template,send_file, jsonify
from werkzeug.utils import secure_filename
import os
from flask import current_app

archivo_bp = Blueprint('archivo_bp', __name__ , static_folder='static' , template_folder='templates')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@archivo_bp.route('/subir_archivo', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            flash('Imagen subida correctamente')

    return render_template('agregar_imagen.html')


@archivo_bp.route('/test', methods=['GET', 'POST'])
def test():

    print(current_app.config["UPLOAD_FOLDER"])
    y = os.listdir(current_app.config["UPLOAD_FOLDER"])
    print(y)
    return '<ul><li>xd</li></ul>'

@archivo_bp.route('/imagenes', methods=['POST'])
def imagenes():

    imagenes = os.listdir(current_app.config["UPLOAD_FOLDER"])
    print(imagenes)
    return render_template('block_imagenes.html', imagenes = imagenes)

# OBTENER IMAGEN DE UN PRODUCTO
@archivo_bp.route('/imagen-producto/<string:nombre>')
def imagen_producto(nombre = None):
	try:
		return send_file('Productos/' + nombre , download_name = nombre)
	except Exception as e:
		return str(e)