
from database import obtener_conexion
from flask import json

class Categoria():
    @classmethod
    def registrar(self,detalle_categoria):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ REGISTRANDO CATEGORIA ------')
                print(detalle_categoria)
                sql = "INSERT INTO categoria(detalle) VALUES(%s)"

                cursor.execute( sql , detalle_categoria)
                print('-'*15)
                miConexion.commit()


        except Exception as ex:
            raise Exception(ex)
        

        finally:
            miConexion.close()
    @classmethod
    def modificar(self,detalle_categoria, id):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ modificando CATEGORIA ------')
                print(detalle_categoria)
                sql = "UPDATE categoria SET detalle = %s where categoria_id = %s"
                cursor.execute( sql , (detalle_categoria , id) )
                print('-'*15)
                miConexion.commit()


        except Exception as ex:
            raise Exception(ex)
        

        finally:
            miConexion.close()
    @classmethod
    def eliminar(self,id):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ eliminando CATEGORIA ------')
                sql = "DELETE FROM categoria  where categoria_id = %s"
                cursor.execute( sql , id )
                print('-'*15)
                miConexion.commit()


        except Exception as ex:
            raise Exception(ex)
        

        finally:
            miConexion.close()
    
    @classmethod
    def obtener_x_id(self, id):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ OBTENIENDO CATEGORIA x ID ------')
                sql = "SELECT categoria_id,detalle from categoria where categoria_id = %s "
                cursor.execute( sql , id )

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
    def obtener_todas(self):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ OBTENIENDO TODAS LAS CATEGORIAS ------')
                sql = "SELECT categoria_id,detalle from categoria"
                cursor.execute( sql )
                resultado = list(cursor.fetchall())
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
    def obtener_inferiores(self):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ OBTENIENDO CATEGORIAS INFERIORES------')
                sql = "SELECT categoria_id, JSON_extract(detalle, '$.nombre_categoria') from categoria WHERE JSON_extract(detalle, '$.tipo_categoria') = 'inferior'"
                cursor.execute( sql )
                resultado = cursor.fetchall()
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
    def obtener_superiores(self):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ OBTENIENDO CATEGORIAS SUPERIORES ------')
                sql = "SELECT categoria_id, JSON_extract(detalle, '$.nombre_categoria') from categoria where JSON_extract(detalle, '$.tipo_categoria') = 'superior'"
                cursor.execute( sql )
                resultado = cursor.fetchall()
                r = json.dumps(resultado)
                resultado = json.loads(r)
                print(resultado)
                
                print('-'*15)
                return resultado

        except Exception as ex:
            raise Exception(ex)
        finally:
            miConexion.close()