from ...extensions import db
from datetime import datetime

class Categoria(db.Model):
  __tablename__ = 'categoria'
  categoria_id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(255), nullable=False)
  nivel = db.Column(db.Integer, nullable=False)
  padre_id = db.Column(db.Integer, db.ForeignKey('categoria.categoria_id'))

class Producto(db.Model):
    __tablename__ = 'producto'
    producto_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255) )
    precio = db.Column(db.Integer)
    categoria = db.Column(db.Integer)
    url_imagen = db.Column(db.String(255))
    imagen_extra = db.Column(db.String(255))
    detalle = db.Column(db.JSON)

class Usuario(db.Model):
  __tablename__ = 'usuario'
  usuario_id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(255))
  apellido = db.Column(db.String(255))
  rut = db.Column(db.String(255))
  correo = db.Column(db.String(255), nullable=True)
  telefono = db.Column(db.String(255))
  contrasena = db.Column(db.String(255), nullable=True)

class Cotizacion(db.Model):
  __tablename__ = "cotizacion"
  cotizacion_id = db.Column(db.Integer, primary_key=True)
  fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
  monto_total = db.Column(db.Float)
  usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.usuario_id"))

class Cotizacion_Producto(db.Model):
  __tablename__ = "cotizacion_producto"
  cotizacion_id = db.Column(db.Integer, db.ForeignKey("cotizacion.cotizacion_id"), primary_key=True)
  producto_id = db.Column(db.Integer, db.ForeignKey("producto.producto_id"), primary_key=True)
  cantidad = db.Column(db.Float)