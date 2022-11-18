import sqlite3 as sqlite3


def insertdestino(  d_lugar,
                    d_dias,
                    d_pension,
                    d_salida,
                    d_regreso,
                    d_costo) :

    conn = sqlite3.connect('db')
    cursor = conn.cursor()
    instruccion = f"insert into Home_destino values ('{d_lugar}', {d_dias}, '{d_pension}', '{d_salida}', '{d_regreso}', {d_costo})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insertdestino ('Buenos Aries', 4,'sin nada de nada', '2022-11-18', '2022-11-25', 215885385.20)


