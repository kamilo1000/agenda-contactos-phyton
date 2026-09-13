
from flask import Flask, render_template, request,redirect                 #importa la clase principal Flask 
import sqlite3



app = Flask(__name__)                     #crea una instancia (u objeto) de la clase Flask y lo guarda en la variable app
                                          # __name__: es una variable especial de Python le dice a Flask donde buscar


@app.route('/')                           #es un decorador de python. modifica el comportamiento de la funcion que viene abajo
def home():
    conc = sqlite3.connect('agenda.db')
    curs = conc.cursor()

    curs.execute("""
        SELECT Nombre, telefono FROM agenda
    """)
    contactos = curs.fetchall()

    return render_template('index.html', agenda_con = contactos)        #procesa archivos de plantillas html usando el jinja pata mostrarlos en el navegador



@app.route('/agregar', methods=['POST'])
def agrega():
    nombre = request.form["Nom"]

    telefono = request.form["Tel"]

    conc = sqlite3.connect('agenda.db')
    curs = conc.cursor()

    curs.execute("""   
        INSERT INTO agenda VALUES
        (?,?)
    """,(nombre, telefono)
    )
    conc.commit()

    return redirect('/')


if __name__ == '__main__':                #asegura que el servidor web solo se encienda si ejecutas este archivo directamente
                                          #evita que el servidor se active por accidente si en el futuro decides impotar este archivo desde otro script de python
    app.run(debug=True)                   #enciende el servidor de desarrollo local integrado de Flask