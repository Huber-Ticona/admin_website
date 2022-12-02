
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

    #-------- new version -------------

    @classmethod
    def registrar_categorias_v2(self,detalle):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ REGISTRANDO CATEGORIA v2------')
                print(detalle)
                sql = "INSERT INTO categoria2(nombre,nivel,padre_id) VALUES(%s,%s,%s)"

                cursor.execute( sql , (detalle['nombre_categoria'] , detalle['nivel'],detalle['padre_id']))
                print('-'*15)
                miConexion.commit()
                

        except Exception as ex:
            raise Exception(ex)
        finally:
            miConexion.close()
    @classmethod
    def obtener_categoriasv2(self):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ OBTENIENDO CATEGORIAS v2 ------')
                sql = '''
                with vista as(
                select  c.categoria_id as id , c.nombre , b.nombre as padre,b.categoria_id as padre_id , c.nivel
                from categoria2 c left join categoria2 b ON b.categoria_id = c.padre_id
                )
                select * from vista
                order by nivel asc
                '''
                cursor.execute( sql )
                resultado = cursor.fetchall()
                #r = json.dumps(resultado)
                #resultado = json.loads(r)
                print(resultado)
                
                print('-'*15)
                return resultado

        except Exception as ex:
            raise Exception(ex)
        finally:
            miConexion.close()

    @classmethod
    def obtener_categorias_arbol(self):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ OBTENIENDO CATEGORIAS v2 ------')
                sql = '''
                with vista as ( 
                select c.categoria_id as padre_id , c.nombre as padre ,d.categoria_id  as hijo_id ,d.nombre as hijo
                from categoria2 c inner join categoria2 d ON  c.categoria_id = d.padre_id
                where c.nivel = 1
                ),
                vista2 as (
                select c.* ,d.categoria_id , d.nombre 
                from vista c inner join categoria2 d on c.hijo_id = d.padre_id
                )
                select concat(padre_id,',',hijo_id,',',categoria_id),concat(padre,' -> ',hijo,' -> ',nombre) from vista2 
                '''
                cursor.execute( sql )
                resultado = cursor.fetchall()
                #r = json.dumps(resultado)
                #resultado = json.loads(r)
                print(resultado)
                
                print('-'*15)
                return resultado

        except Exception as ex:
            raise Exception(ex)
        finally:
            miConexion.close()