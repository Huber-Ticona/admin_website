from ...extensions import obtener_conexion
class control_Categoria():

    @classmethod
    def obtener_categorias_v2(self):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ OBTENIENDO CATEGORIAS  ------')
                sql = '''
                with vista as(
                select  c.categoria_id as id , c.nombre , b.nombre as padre,b.categoria_id as padre_id , c.nivel
                from categoria c left join categoria b ON b.categoria_id = c.padre_id
                )
                select * from vista
                order by nivel asc
                '''
                cursor.execute( sql )
                resultado = cursor.fetchall()
                #r = json.dumps(resultado)
                #resultado = json.loads(r)
                #print(resultado)
                
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
                print('------ OBTENIENDO CATEGORIAS arbol v2 ------')
                sql = '''
                with vista as ( 
                select c.categoria_id as padre_id , c.nombre as padre ,d.categoria_id  as hijo_id ,d.nombre as hijo
                from categoria c inner join categoria d ON  c.categoria_id = d.padre_id
                where c.nivel = 1
                ),
                vista2 as (
                select c.* ,d.categoria_id , d.nombre 
                from vista c inner join categoria d on c.hijo_id = d.padre_id
                )
                select concat(padre_id,',',hijo_id,',',categoria_id),concat(padre,' -> ',hijo,' -> ',nombre),categoria_id from vista2 
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
    def obtener_rutas(self):
        miConexion = obtener_conexion()
        try:
            with miConexion.cursor() as cursor:
                print('------ OBTENIENDO RUTAS  ------')
                sql = '''
                WITH RECURSIVE rutas (categoria_id, nombre, nivel, ruta) AS (
                SELECT c.categoria_id, c.nombre, c.nivel, c.nombre
                FROM categoria c
                WHERE c.padre_id IS NULL
                UNION ALL
                SELECT c.categoria_id, c.nombre, c.nivel, CONCAT(r.ruta, '/', c.nombre)
                FROM categoria c
                INNER JOIN rutas r ON c.padre_id = r.categoria_id
                )
                SELECT r.categoria_id, r.nombre, r.nivel, r.ruta
                FROM rutas r;
                '''
                cursor.execute( sql )
                resultado = cursor.fetchall()
                #r = json.dumps(resultado)
                #resultado = json.loads(r)
                #print(resultado)
                
                print('-'*15)
                return resultado

        except Exception as ex:
            raise Exception(ex)
        finally:
            miConexion.close()