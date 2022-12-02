from database import obtener_conexion
from flask import json

class Producto():

    @classmethod
    def registrar(self,datos):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ REGISTRANDO PRODUCTO ------')

                print(datos)
                cates = datos['cat'].split(',')
                cates =  [int(x) for x in cates]
                print(cates)
                detalle = json.dumps({
                    'categoria':cates,
                    'descripcion':datos['descripcion_producto']
                })
                cates= json.dumps(cates)
                print(detalle)
                sql = "INSERT INTO producto(nombre,categoria,precio,url_imagen,imagen_extra,descripcion,detalle) VALUES(%s,%s,%s,%s,%s,%s,%s)"

                cursor.execute( sql ,( datos['nombre_producto'], cates , datos['precio_producto'],datos['url_imagen'],datos['imagen_extra'],datos['descripcion_producto'],detalle) )
                print('-'*15)
                miConexion.commit()


        except Exception as ex:
            raise Exception(ex)
        

        finally:
            miConexion.close()

    @classmethod
    def obtener_todos(self):
        x = 0
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ OBTENIENDO PRODUCTOS ------')
                sql = "SELECT producto_id,nombre,categoria,precio,url_imagen,imagen_extra from producto"
                cursor.execute( sql )
                resultado = list(cursor.fetchall())
                r = json.dumps(resultado)
                resultado = json.loads(r)
                #print(resultado)
                
                print('-'*15)
                return resultado

        except Exception as ex:
            raise Exception(ex)
        finally:
            miConexion.close()

    @classmethod
    def obtener_x_id(self, id):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print(f'------ OBTENIENDO PRODUCTO ID: {str(id)}  ------')
                #sql = "SELECT JSON_EXTRACT(categoria.detalle, '$.nombre_categoria'), producto.*  FROM ( producto inner join categoria ON producto.categoria = categoria.categoria_id) WHERE producto_id = %s"
                sql = "SELECT * FROM producto WHERE producto_id = %s "
                cursor.execute( sql , id)
                resultado = list(cursor.fetchone())
                r = json.dumps(resultado)
                resultado = json.loads(r)
                print(resultado)
                print('-'*15)
                return resultado

        except Exception as ex:
            raise Exception(ex)
        finally:
            miConexion.close()
            
    @classmethod
    def modificar(self, id, dato):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print(f'------ MODIFICANDO PRODUCTO ID: {str(id)}  ------')
                sql = "UPDATE producto SET nombre = %s ,descripcion = %s ,categoria = %s ,precio = %s ,url_imagen = %s,imagen_extra = %s  WHERE producto_id = %s "
                cursor.execute( sql, ( dato['nombre_producto'] , dato['descripcion_producto'], dato['categoria_producto'] ,dato['precio_producto'],dato['url_imagen'],dato['imagen_extra'] , id) )
                print('-'*15)
                miConexion.commit()

        except Exception as ex:
            raise Exception(ex)
        finally:
            miConexion.close()

    @classmethod
    def eliminar(self, id):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print(f'------ eliminando PRODUCTO {str(id)}------')
                sql = "DELETE FROM producto  where producto_id = %s"
                cursor.execute( sql , id )
                print('-'*15)
                miConexion.commit()

        except Exception as ex:
            raise Exception(ex)
        finally:
            miConexion.close()
