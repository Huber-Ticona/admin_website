from ...extensions import db


class Categoria(db.Model):
    __tablename__ = 'categoria'
    categoria_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    nivel = db.Column(db.Integer)
    padre_id = db.Column(db.Integer)




class Producto(db.Model):
    __tablename__ = 'producto'
    producto_id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(255) )
    precio = db.Column(db.Integer)
    categoria = db.Column(db.Integer)

    url_imagen = db.Column(db.String(255))
    imagen_extra = db.Column(db.String(255))
    
    detalle = db.Column(db.JSON)