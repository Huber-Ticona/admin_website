from flask import Blueprint, render_template,url_for,request,jsonify,json,flash,redirect

from .models.entities.models import Categoria, Producto
from .models.controllers.controlCategoria import control_Categoria
from .models.controllers.controlProducto import control_Producto
from .extensions import db

main = Blueprint('main', __name__ )

@main.route('/')
@main.route('/inicio')
def inicio():
    return render_template('inicio.html')
    
@main.route('/agregar/producto' , methods=['POST' , 'GET'])
def agregar_producto():
    if request.method == 'POST':
        print('ingresando producto ...')
        dato = request.json
        #producto = Producto()
        #(nombre,categoria,precio,url_imagen,imagen_extra,descripcion,detalle)
        #producto.nombre = dato['nombre_producto']
        #producto.categoria = l_categorias
        #producto.precio = dato['precio']
        #producto.url_imagen = dato['url_imagen']
        #producto.imagen_extra = dato['imagen_extra']
        #db.session.add(producto)
        #db.session.commit()
        control_Producto.registrar(dato)
        return jsonify(data = True, mensaje = "Producto: " + dato['nombre_producto'] + " Agregado con exito.")      

    #categorias = Categoria.obtener_inferiores()
    categoria  = control_Categoria.obtener_categorias_arbol()

    print('vista agregar producto')
    return render_template('agregar_producto.html' , categorias = categoria )

  
@main.route('/modificar/producto/<int:producto_id>', methods=['POST', 'GET'])
def modificar_producto(producto_id = None):

    #PROTECCION XSS - VERIFICADA : solo admite numeros enteros
    if request.method == 'POST':
        print(f'------ POST MODIFICAR PRODUCTO {str(producto_id)} --------')
        dato = request.json
        print('JSON',dato) #NO USAR JSON DUMPS

        control_Producto.modificar(producto_id, dato)
        print('-'*15)
        return jsonify(estado = True, mensaje = 'RECIBIDO, Producto modiicado correctamente')
        
    producto = control_Producto.obtener_x_id(producto_id)
    categorias  = control_Categoria.obtener_categorias_arbol()
    return render_template('agregar_producto.html', producto = producto , categorias = categorias )
    
@main.route('/visualizar/producto')
def visualizar_producto():
    productos = control_Producto.obtener_todos()
    return render_template('lista_productos.html', productos = productos)
  
@main.route('/eliminar/producto/<int:id>')
def eliminar_producto(id= None):
    print(f'------- eliminando producto {id}')
    Producto.eliminar(id)
    print('-'*15)
    return jsonify( data = True, mensaje = 'PRODUCTO ELIMINADO CORRECTAMENTE')


###### RUTAS PARA GESTIONAR CATEGORIAS #######



@main.route('/agregar/categoria' , methods=['GET','POST'])
def agregar_categoria():
    if request.method == 'POST':
        print('------- AGREGAR CATEGORIA [POST] -----')
        dato = request.json
        print(dato)
        new_categoria = Categoria(nombre= dato['nombre_categoria'] , nivel= dato['nivel'], padre_id=dato['padre_id']) 
        db.session.add(new_categoria)
        db.session.commit() 

        #redirect(url_for('main.categoria'))
        return jsonify(data = True, mensaje = "Categoria: " + dato['nombre_categoria'] + " Agregado con exito. Actualize la pagina para ver los cambios") 
    
    print('------- AGREGAR CATEGORIA [GET] -----')
    lista_categorias = control_Categoria.obtener_categorias_v2()
    print('------- END -----')
    return render_template('agregar_categoria.html' , categorias = lista_categorias , categoria = None )

    

@main.route('/categoria/modificar/<int:id>' , methods = ['POST', 'GET'])
def modificar_categoria(id = None):
    print('-'*10)
    if request.method == 'POST':
        dato = request.json
        print(dato)
        categoria =  Categoria.query.filter_by(categoria_id = id).first()
        categoria.nombre = dato["nombre_categoria"]
        categoria.nivel = dato["nivel"]
        categoria.padre_id = dato["padre_id"]
        
        db.session.commit()

        return jsonify(data = True, mensaje = "Categoria: " + dato['nombre_categoria'] + " Modificada  con exito. Actualize la pagina para ver los cambios") 

    lista_categorias = control_Categoria.obtener_categorias_v2()
    categoria =  Categoria.query.filter_by(categoria_id = id).first()
    
    return render_template('agregar_categoria.html' , categorias = lista_categorias , categoria = categoria )


@main.route('/categoria/eliminar/<int:id>' , methods = ['POST', 'GET'])
def eliminar_categoria(id = None):
    print('URL PARA ELIMINAR CATEGORIA')
    if id != None:
        categoria =  Categoria.query.filter_by(categoria_id = id).first()
        db.session.delete(categoria)
        db.session.commit() 

        return jsonify(data = True, mensaje = f'categoria: {str(id)}, eliminada con exito ')

@main.route('/visualizar/categoria')
def visualizar_categorias():
    lista_categorias = Categoria.query.order_by(Categoria.nivel.asc()).all()
    return render_template('lista_categorias.html' , categorias = lista_categorias)

@main.errorhandler(404)
def error(e):
    return 'hola error 404',404