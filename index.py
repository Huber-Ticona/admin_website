from flask import Flask, flash, redirect, render_template, session, request, url_for,jsonify, json
from database import obtener_conexion
from modelos.categoria import Categoria
from modelos.producto import Producto
from archivos import archivo_bp

UPLOAD_FOLDER = '../new_website/Productos'

app = Flask(__name__)
app.secret_key = 'madenco_enco_chilemat'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.register_blueprint(archivo_bp, url_prefix='/')

@app.route('/')
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')
    
@app.route('/agregar/producto' , methods=['POST' , 'GET'])
def agregar_producto():
    if request.method == 'POST':
        print('ingresando producto ...')
        dato = request.json

        Producto.registrar(dato)
        return jsonify(data = True, mensaje = "Producto: " + dato['nombre_producto'] + " Agregado con exito.")      

    categorias = Categoria.obtener_inferiores()
    print('vista agregar producto')
    return render_template('agregar_producto.html' , categorias = categorias)

  
@app.route('/modificar/producto/<int:producto_id>', methods=['POST', 'GET'])
def modificar_producto(producto_id = None):
    #PROTECCION XSS - VERIFICADA : solo admite numeros enteros
    if request.method == 'POST':
        print(f'------ POST MODIFICAR PRODUCTO {str(producto_id)} --------')
        dato = request.json
        print('JSON',dato) #NO USAR JSON DUMPS

        Producto.modificar(producto_id, dato)
        print('-'*15)
        return jsonify(estado = True, mensaje = 'RECIBIDO, Producto modiicado correctamente')
        
        

    producto = Producto.obtener_x_id(producto_id)
    categorias = Categoria.obtener_inferiores()
    return render_template('agregar_producto.html', producto = producto , categorias = categorias )
    
@app.route('/visualizar/producto')
def visualizar_producto():
    productos = Producto.obtener_todos()
    return render_template('lista_productos.html', productos = productos)
  
@app.route('/eliminar/producto/<int:id>')
def eliminar_producto(id= None):
    print(f'------- eliminando producto {id}')
    Producto.eliminar(id)
    print('-'*15)
    return jsonify( data = True, mensaje = 'PRODUCTO ELIMINADO CORRECTAMENTE')

@app.route('/agregar/categoria' , methods=['POST', 'GET'])
def agregar_categoria():
    if request.method == 'POST':
        print('ingresando CATEGORIA ...')
        dato = request.json
        detalle = json.dumps(dato)
        Categoria.registrar(detalle)
        return jsonify(data = True, mensaje = "Categoria: " + dato['nombre_categoria'] + " Agregado con exito. Actualize la pagina para ver los cambios") 
         
    print('se muestra la vista get')
    categorias_superiores = Categoria.obtener_superiores()

    return render_template('agregar_categoria.html' , vista = 'agregar' ,superiores = categorias_superiores)

@app.route('/categoria/modificar/<string:id>' , methods = ['POST', 'GET'])
def modificar_categoria(id = None):
    print('-'*10)
    if request.method == 'POST':
        print('modificcando ... categoria ')
        dato = request.json
        print(dato)
        detalle = json.dumps(dato)

        Categoria.modificar(detalle_categoria=detalle,id=id )
        return jsonify(data = True, mensaje = "Categoria: " + dato['nombre_categoria'] + " Modificada  con exito. Actualize la pagina para ver los cambios") 
         
    
    print('vista modificar  categoria ... ')
    categoria = Categoria.obtener_x_id(id)
    categorias_superiores = Categoria.obtener_superiores()
    return render_template('agregar_categoria.html' , vista='modificar' , categoria = categoria, superiores = categorias_superiores)

@app.route('/categoria/eliminar/<int:id>' , methods = ['POST', 'GET'])
def eliminar_categoria(id = None):
    print('URL PARA ELIMINAR CATEGORIA ')
    if id != None:
        Categoria.eliminar(id)
        return jsonify(data = True, mensaje = f'eliminado con exito {str(id)}')

@app.route('/visualizar/categoria')
def visualizar_categorias():

    resultado = Categoria.obtener_todas()
    
    return render_template('lista_categorias.html' , categorias = resultado)

@app.errorhandler(404)
def error(e):
    return 'hola error 404',404

if __name__ == '__main__':
    app.run(debug=True, port=5002 , host='0.0.0.0')

