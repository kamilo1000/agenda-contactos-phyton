import sqlite3

def agregar_cont():                      #funcion que agrega contacto 

    try:
        clave = input("Nombre \n ")
        valor = input("Telefono \n")

        curs.execute("""
            INSERT INTO agenda VALUES
            (?, ?)
        """, (clave, valor)                 
        )                              #inserta los valores a la tabla
        conec.commit()
        return

    except sqlite3.Error:
        return print("El contacto ya existe")


def ver_cont():                         #funcion para ver todos los contactos
    curs.execute("""        
        SELECT 1 FROM agenda LIMIT 1
    """)                                # "LIMIT 1" mira si existe al menos una fila 
    result = curs.fetchone()     #  recupera la siguiente fila de una consulta de SQL devolviendo una tupla o None si no hay registros

    if result is None:
        print("\n No tiene contactos agregados \n")
        return
    else:
        curs.execute("""
            SELECT Nombre, Telefono FROM agenda
        """)
    print(curs.fetchall())
    return


def buscar_cont():
    curs.execute("""
        SELECT 1 FROM agenda LIMIT 1
    """)
    rst = curs.fetchone()

    if rst is None:
        print("\n No tiene contactos agregados \n")
    else:
        bus_cont = input("\n Esciba el nombre del contacto \n")

        curs.execute("""
            SELECT Nombre, Telefono FROM agenda WHERE Nombre = ?
        """, (bus_cont,)
        )
        rstp = curs.fetchone()

        if rstp is None:
            print("\n No existe contacto \n")
            return
        else: 
            print(f" Nombre: {rstp[0]}\n Telefono: {rstp[1]}")
            return


def modif_cont():                               # funcion para modificar el numero de un contacto
    mdf = input("\n Escriba el nombre del contacto \n")

    curs.execute("""
        SELECT Nombre FROM agenda WHERE Nombre = ?
    """, (mdf,)
    )
    rst1 = curs.fetchone()

    if rst1 is None:
        print("\n El contacto no existe")
        return
    else:
        num_nu = input("\n Digite el nuevo numero \n")
        curs.execute("""
            UPDATE agenda
            SET Telefono = ?
            WHERE Nombre = ?
        """,(num_nu, mdf)
        )
        conec.commit()
        return


def borr_cont():                        # funcion para borrar contactos con el nombre
    borr = input("\n Escriba el nombre del contacto \n")

    curs.execute("""
        SELECT Nombre FROM agenda WHERE Nombre = ?
    """, (borr,)
    )

    rst2 = curs.fetchone()

    if rst2 is None:
        print("\n El contacto no existe")
        return
    else:
        curs.execute("""
            DELETE FROM agenda
            WHERE Nombre = ?
        """, (borr,)
        )
        print("\n contacto eliminado \n")
        conec.commit()
        return


conec = sqlite3.connect("agenda.db")
curs = conec.cursor()

curs.execute("""
    CREATE TABLE IF NOT EXISTS agenda (
    Nombre TEXT UNIQUE,
    Telefono TEXT UNIQUE
    )
""")

while True:
    try: 
        opcion = int(input("\n Que desea hacer digite la opcion que quiera \n 1. Agregar \n 2. Ver todos \n 3. Buscar \n 4. Modificar \n 5. Borrar \n 6. Salir \n"))

        if opcion == 1: 
            agregar_cont()
        elif opcion == 2:
            ver_cont()
        elif opcion == 3:
            buscar_cont()
        elif opcion == 4:
            modif_cont()
        elif opcion == 5:
            borr_cont()
        elif opcion == 6:
            conec.close()
            break
        else:
            print("\n Digite un numero que coresponda a la opcion \n")
    except ValueError:
        print("\n Digite un numero")