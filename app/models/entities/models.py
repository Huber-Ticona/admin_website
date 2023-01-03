from ...extensions import db


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
