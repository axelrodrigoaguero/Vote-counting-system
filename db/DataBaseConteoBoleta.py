import psycopg2
from Model.Votos_lista_completa import Votos_lista_completa
from Model.Votos_personalizado import Votos_personalizado
from Model.Votos_blanco import Votos_blanco
from Model.Votos_nulos import Votos_nulos
from Model.Data_sheet import Data_sheet



class ConteoBotosDB:
    def __init__(self):
        self.connection = psycopg2.connect(host="localhost", database="ConteoVotosBoleta", user="postgres",
                                           port="5432",
                                           password="lucas3030")
        self.cursor = self.connection.cursor()

        #postgres://lucascasado302000:F8Oj9DPkgSHb@ep-nameless-morning-833149.us-east-2.aws.neon.tech/conteo_votos
    

    # VOTOS LISTA COMPLETA
    def insertVotosBoleta1(self, boleta1: Votos_lista_completa):
        SQLinsert = f"insert into votos_lista_completa(boleta1, boleta2, boleta3) values ('{boleta1.boleta1}','{boleta1.boleta2}','{boleta1.boleta3}');"
        self.cursor.execute(SQLinsert)
        self.connection.commit()


    def insertVotosBoleta2(self, boleta2: Votos_lista_completa):
        SQLinsert = f"insert into votos_lista_completa(boleta1, boleta2, boleta3) values ('{boleta2.boleta1}','{boleta2.boleta2}','{boleta2.boleta3}');"
        self.cursor.execute(SQLinsert)
        self.connection.commit()


    def insertVotosBoleta3(self, boleta3: Votos_lista_completa):
        SQLinsert = f"insert into votos_lista_completa(boleta1, boleta2, boleta3) values ('{boleta3.boleta1}','{boleta3.boleta2}','{boleta3.boleta3}');"
        self.cursor.execute(SQLinsert)
        self.connection.commit()  

    
    
    # VOTOS LISTA PERSONALIZADA
    def insertVotosPersonalizados(self, votos_personalizados: Votos_personalizado):
        SQLinsert = f"INSERT INTO votos_personalizado(intendente1, intendente2, intendente3, concejal1, concejal2, concejal3) VALUES ('{votos_personalizados.intendente1}', '{votos_personalizados.intendente2}', '{votos_personalizados.intendente3}', '{votos_personalizados.concejal1}', '{votos_personalizados.concejal2}', '{votos_personalizados.concejal3}');"
        self.cursor.execute(SQLinsert)
        self.connection.commit()



    # VOTOS NULOS
    def insertVotosNulos(self, votos_nulos: Votos_nulos):
        SQLinsert = f"INSERT INTO votos_nulos(votos) VALUES ('{votos_nulos.votos}');"
        self.cursor.execute(SQLinsert)
        self.connection.commit()

    
    # GET VOTOS NULOS
    def getAllVotosNulos(self):
        self.cursor.execute("SELECT * FROM votos_nulos ORDER BY id")
        votos_nulos = self.cursor.fetchall()
        return votos_nulos



    # VOTOS BLANCO
    def insertVotosBlanco(self, votos_blanco: Votos_blanco):
        SQLinsert = f"INSERT INTO votos_blanco(votos) VALUES ('{votos_blanco.votos}');"
        self.cursor.execute(SQLinsert)
        self.connection.commit()


    # GET VOTOS BLANCO
    def getAllVotosBlanco(self):
        self.cursor.execute("SELECT * FROM votos_blanco ORDER BY id")
        votos_blanco = self.cursor.fetchall()
        return votos_blanco



    # INSERT DATA SHEET
    def insertDataSheet(self, data_sheet: Data_sheet):
        SQLinsert = f"INSERT INTO data_sheet(departamento, circuito, mesa, electores, boletas, diferencia) VALUES ('{data_sheet.departamento}', '{data_sheet.circuito}', '{data_sheet.mesa}', '{data_sheet.electores}', '{data_sheet.boletas}', '{data_sheet.diferencia}');"
        self.cursor.execute(SQLinsert)
        self.connection.commit()


    # GET DATA SHEET
    def getAllDataSheet(self):
        self.cursor.execute("SELECT * FROM data_sheet ORDER BY id")
        data_sheet = self.cursor.fetchall()
        return data_sheet






    # BORRAR ALL VOTOS LISTA COMPLETA
    def deleteAllVotosCompleta(self):
        SQLdelete = "DELETE FROM votos_lista_completa;"
        self.cursor.execute(SQLdelete)
        self.connection.commit()

    # BORRAR ALL VOTOS LISTA PERSONALIZADA
    def deleteAllVotosPersonalizo(self):
        SQLdelete = "DELETE FROM votos_personalizado;"
        self.cursor.execute(SQLdelete)
        self.connection.commit()

    # BORRAR ALL VOTOS NULOS
    def deleteAllVotosNulos(self):
        SQLdelete = "DELETE FROM votos_nulos;"
        self.cursor.execute(SQLdelete)
        self.connection.commit()

    # BORRAR ALL VOTOS BLANCO
    def deleteAllVotosBlanco(self):
        SQLdelete = "DELETE FROM votos_blanco;"
        self.cursor.execute(SQLdelete)
        self.connection.commit()


    
    # BORRAR ALL DATA SHEET
    def deleteAllDataSheet(self):
        SQLdelete = "DELETE FROM data_sheet;"
        self.cursor.execute(SQLdelete)
        self.connection.commit()

    


    # ARREGLAR DETALLES
    # def obtenerTotalVotosPersonalizados(self):
    #     SQLselect = "SELECT (COALESCE(intendente1, 0) + COALESCE(intendente2, 0) + COALESCE(intendente3, 0) + COALESCE(concejal1, 0) + COALESCE(concejal2, 0) + COALESCE(concejal3, 0)) AS TotalVotos FROM votos_personalizado;"
    #     self.cursor.execute(SQLselect)
    #     result = self.cursor.fetchone()
    #     print("Total de votos personalizados:", result[0])

    # def obtenerTotalVotosListaCompleta(self):
    #     SQLselect = "SELECT (COALESCE(boleta1, 0) + COALESCE(boleta2, 0) + COALESCE(boleta3, 0)) AS TotalVotos FROM votos_lista_completa;"
    #     self.cursor.execute(SQLselect)
    #     result = self.cursor.fetchone()
    #     print("Total de votos lista completa:", result[0])










    def obtenerCantidadVotosEmitidos(self):
        SQLselect = "SELECT SUM(boleta1 + boleta2 + boleta3) AS TotalVotos FROM votos_lista_completa;"
        self.cursor.execute(SQLselect)
        result = self.cursor.fetchone()
        print("Total de votos:", result)
        return result[0]
    












    # VOTO LISTA COMPLETA
    def obtenerBoletaGanadora(self):
        SQLselect = "SELECT CASE WHEN boleta1 >= boleta2 AND boleta1 >= boleta3 THEN 'Boleta 1' WHEN boleta2 >= boleta1 AND boleta2 >= boleta3 THEN 'Boleta 2' ELSE 'Boleta 3' END AS Ganadora FROM votos_lista_completa;"
        self.cursor.execute(SQLselect)
        result = self.cursor.fetchone()
        boleta_ganadora = result[0]
        print("Boleta ganadora:", boleta_ganadora)
        self.connection.commit()  # Guardar los cambios en la base de datos
        return boleta_ganadora

    def obtenerVotosGanadora(self):
        SQLselect = "SELECT GREATEST(boleta1, boleta2, boleta3) AS VotosImpuestos FROM votos_lista_completa;"
        self.cursor.execute(SQLselect)
        result = self.cursor.fetchone()
        votos_impuestos = result[0]
        print("Se impuso con", votos_impuestos, "votos")
        self.connection.commit()  # Guardar los cambios en la base de datos
        return votos_impuestos










    # VOTO LISTA PERSONALIZADA
    def obtenerBoletaGanadoraPersonalizada(self):
        SQLselect = """
            SELECT CASE
                WHEN (COALESCE(SUM(intendente1), 0) + COALESCE(SUM(concejal1), 0)) >= (COALESCE(SUM(intendente2), 0) + COALESCE(SUM(concejal2), 0))
                    AND (COALESCE(SUM(intendente1), 0) + COALESCE(SUM(concejal1), 0)) >= (COALESCE(SUM(intendente3), 0) + COALESCE(SUM(concejal3), 0))
                    THEN 'Boleta 1'
                WHEN (COALESCE(SUM(intendente2), 0) + COALESCE(SUM(concejal2), 0)) >= (COALESCE(SUM(intendente1), 0) + COALESCE(SUM(concejal1), 0))
                    AND (COALESCE(SUM(intendente2), 0) + COALESCE(SUM(concejal2), 0)) >= (COALESCE(SUM(intendente3), 0) + COALESCE(SUM(concejal3), 0))
                    THEN 'Boleta 2'
                ELSE 'Boleta 3'
            END AS Ganadora
            FROM votos_personalizado;
        """
        self.cursor.execute(SQLselect)
        result = self.cursor.fetchone()
        boleta_ganadora = result[0]
        print("Boleta ganadora personalizada:", boleta_ganadora)
        self.connection.commit()
        return boleta_ganadora

    def obtenerVotosGanadoraPersonalizada(self):
        SQLselect = """
            SELECT GREATEST(
                COALESCE(SUM(intendente1), 0) + COALESCE(SUM(concejal1), 0),
                COALESCE(SUM(intendente2), 0) + COALESCE(SUM(concejal2), 0),
                COALESCE(SUM(intendente3), 0) + COALESCE(SUM(concejal3), 0)
            ) AS VotosImpuestos
            FROM votos_personalizado;
        """
        self.cursor.execute(SQLselect)
        result = self.cursor.fetchone()
        votos_impuestos = result[0]
        print("Se impuso con", votos_impuestos, "votos")
        self.connection.commit()
        return votos_impuestos






















    # GANADOR DEFINITIVO
    # def obtenerGanadorDefinitivo(self):
    #     SQLselect = "SELECT CASE WHEN COALESCE(vl.boleta1, 0) + COALESCE(vp.intendente1, 0) + COALESCE(vp.concejal1, 0) >= COALESCE(vl.boleta2, 0) + COALESCE(vp.intendente2, 0) + COALESCE(vp.concejal2, 0) AND COALESCE(vl.boleta1, 0) + COALESCE(vp.intendente1, 0) + COALESCE(vp.concejal1, 0) >= COALESCE(vl.boleta3, 0) + COALESCE(vp.intendente3, 0) + COALESCE(vp.concejal3, 0) THEN 'Boleta 1' WHEN COALESCE(vl.boleta2, 0) + COALESCE(vp.intendente2, 0) + COALESCE(vp.concejal2, 0) >= COALESCE(vl.boleta1, 0) + COALESCE(vp.intendente1, 0) + COALESCE(vp.concejal1, 0) AND COALESCE(vl.boleta2, 0) + COALESCE(vp.intendente2, 0) + COALESCE(vp.concejal2, 0) >= COALESCE(vl.boleta3, 0) + COALESCE(vp.intendente3, 0) + COALESCE(vp.concejal3, 0) THEN 'Boleta 2' ELSE 'Boleta 3' END AS Ganadora FROM votos_lista_completa vl, votos_personalizado vp;"
    #     self.cursor.execute(SQLselect)
    #     result = self.cursor.fetchone()
    #     ganador = result[0]
    #     self.connection.commit()  # Guardar los cambios en la base de datos
    #     return ganador

    # def obtenerVotosImpuestos(self):
    #     SQLselect = "SELECT COALESCE(vl.boleta1, 0) + COALESCE(vp.intendente1, 0) + COALESCE(vp.concejal1, 0) + COALESCE(vl.boleta2, 0) + COALESCE(vp.intendente2, 0) + COALESCE(vp.concejal2, 0) + COALESCE(vl.boleta3, 0) + COALESCE(vp.intendente3, 0) + COALESCE(vp.concejal3, 0) AS VotosImpuestos FROM votos_lista_completa vl, votos_personalizado vp;"
    #     self.cursor.execute(SQLselect)
    #     result = self.cursor.fetchone()
    #     votos_impuestos = result[0]
    #     self.connection.commit()  # Guardar los cambios en la base de datos
    #     return votos_impuestos


    def obtenerGanadorFinal(self):
        SQLselect_lista_completa = """
            SELECT 'Boleta 1' AS boleta, SUM(boleta1) AS total_votos FROM votos_lista_completa
            UNION ALL
            SELECT 'Boleta 2' AS boleta, SUM(boleta2) AS total_votos FROM votos_lista_completa
            UNION ALL
            SELECT 'Boleta 3' AS boleta, SUM(boleta3) AS total_votos FROM votos_lista_completa
        """
        self.cursor.execute(SQLselect_lista_completa)
        result_lista_completa = self.cursor.fetchall()

        max_votos_lista_completa = max(result_lista_completa, key=lambda x: x[1])
        votos_max_lista_completa = max_votos_lista_completa[1]
        boletas_ganadoras_lista_completa = [result[0] for result in result_lista_completa if result[1] == votos_max_lista_completa]

        SQLselect_personalizada = """
            SELECT 'Boleta 1' AS boleta, SUM(intendente1 + concejal1) AS total_votos FROM votos_personalizado
            UNION ALL
            SELECT 'Boleta 2' AS boleta, SUM(intendente2 + concejal2) AS total_votos FROM votos_personalizado
            UNION ALL
            SELECT 'Boleta 3' AS boleta, SUM(intendente3 + concejal3) AS total_votos FROM votos_personalizado
        """
        self.cursor.execute(SQLselect_personalizada)
        result_personalizada = self.cursor.fetchall()

        max_votos_personalizada = max(result_personalizada, key=lambda x: x[1])
        votos_max_personalizada = max_votos_personalizada[1]
        boletas_ganadoras_personalizada = [result[0] for result in result_personalizada if result[1] == votos_max_personalizada]

        ganador_final = None

        if len(boletas_ganadoras_lista_completa) > 1 or len(boletas_ganadoras_personalizada) > 1:
            # Hay empate en la cantidad máxima de votos, se determina el ganador comparando los votos personalizados
            max_votos_personalizada = max(result_personalizada, key=lambda x: x[1] if x[0] in boletas_ganadoras_lista_completa else 0)
            ganador_final = max_votos_personalizada[0]
        else:
            # No hay empate, se determina el ganador comparando la cantidad máxima de votos en ambas listas
            ganador_final = boletas_ganadoras_lista_completa[0] if votos_max_lista_completa > votos_max_personalizada else boletas_ganadoras_personalizada[0]

        print("Boleta ganadora final:", ganador_final)
        self.connection.commit()

        return ganador_final
















    def obtenerVotosImpuestosListaCompleta(self, boleta_ganadora):
        SQLselect = """
            SELECT CASE
                WHEN 'Boleta 1' = %s THEN SUM(boleta1)
                WHEN 'Boleta 2' = %s THEN SUM(boleta2)
                WHEN 'Boleta 3' = %s THEN SUM(boleta3)
                ELSE 0
            END AS VotosImpuestos
            FROM votos_lista_completa;
        """
        self.cursor.execute(SQLselect, (boleta_ganadora, boleta_ganadora, boleta_ganadora))
        result = self.cursor.fetchone()
        votos_impuestos = result[0] if result else 0

        print("La boleta ganadora en lista completa se impuso con", votos_impuestos, "votos")
        self.connection.commit()

        return votos_impuestos




    def obtenerVotosImpuestosPersonalizada(self, boleta_ganadora):
        SQLselect = """
            SELECT CASE
                WHEN 'Boleta 1' = %s THEN SUM(intendente1 + concejal1)
                WHEN 'Boleta 2' = %s THEN SUM(intendente2 + concejal2)
                WHEN 'Boleta 3' = %s THEN SUM(intendente3 + concejal3)
                ELSE 0
            END AS VotosImpuestos
            FROM votos_personalizado;
        """
        self.cursor.execute(SQLselect, (boleta_ganadora, boleta_ganadora, boleta_ganadora))
        result = self.cursor.fetchone()
        votos_impuestos = result[0] if result else 0

        print("La boleta ganadora en lista personalizada se impuso con", votos_impuestos, "votos")
        self.connection.commit()

        return votos_impuestos
