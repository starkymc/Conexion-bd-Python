from flask import Flask, redirect, render_template,flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from models.forms.loginmodel import LoginForm
from models.forms.salonmodel import SalonForm
from models.forms.alumnomodel import AlumnoForm

import os

app= Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)



@app.route("/", methods = ['GET', 'POST'])
def login():
    
    formulario = LoginForm()

    if formulario.validate_on_submit():
        flash('Inicio de sesion solicitado por {}, ¿Recordar?={}'
              .format(formulario.username.data, formulario.remember_me.data))
        return redirect(url_for('indexcss'))

    return render_template("login.html", form = formulario)

@app.route("/css")
def indexcss():
    return render_template("indexcss.html")


@app.route("/prueba")
def prueba():
    return render_template("prueba.html")



@app.route("/registroSalon", methods=['GET', 'POST'])
#Nombre de la funcion
def registroSsalon():        
    #Instanciando como objeto la clase SalonForm de forms   
    formSalon = SalonForm()  
    #usamos el objeto y validamos si no esta vacio al dar clic en el boton
    if formSalon.validate_on_submit(): 
        #Importamos la clase Salon de db
        from models.db.salonmodel import Salon  
        #Usamos la clase que importamos creando una variable
        s1 = Salon(aula=formSalon.aula.data, horaEntrada=formSalon.horaEntrada.data)
       
        #Agregamos el registro 
        db.session.add(s1)
        #Confirmamos el registro
        db.session.commit()
        #Redirige a la funcion
        return redirect(url_for('registroSsalon'))
    #Si esta vacio lo valida y redirige a registroSalon.html con los campos requeridos
    return render_template("registroSalon.html", formS= formSalon)



@app.route("/registroSalonAlumno", methods=['GET', 'POST'])
#Nombre de la funcion
def registroSalonAlumno():
     #Instanciando como objeto la clase SalonForm de forms   
    formSalon = SalonForm()
    formAlumno = AlumnoForm()
    #usamos los objetos y validamos los campos que pusimos
    # en Required en los forms que no este vacio al momento de dar clic en el boton
    if formSalon.validate_on_submit() and formAlumno.validate_on_submit():
        #Importamos la clase Salon de db
        from models.db.alumnomodel import Alumno
        from models.db.salonmodel import Salon
        #Usamos la clase que importamos creando una variable
        s1 = Salon(aula=formSalon.aula.data, horaEntrada=formSalon.horaEntrada.data)
        a1 = Alumno(id=int(formAlumno.id.data), nombre=formAlumno.nombre.data, apellido=formAlumno.apellido.data, salon=s1)
         #Agregamos los registros
        db.session.add(s1)
        db.session.add(a1)
        #Confirmamos el registro
        db.session.commit()
        #Redirige a la funcion
        return redirect(url_for('registroSalonAlumno'))

    #Si esta vacio lo valida y redirige a registroSalonAlumno.html con los campos requeridos
    return render_template("registroSalonAlumno.html", formA = formAlumno, formS = formSalon)


#Prueba mandando defrente los datos sin forms
def insert_record():
    from models.db.salonmodel import Salon
    from models.db.alumnomodel import Alumno

    s1 = Salon(aula="B",horaEntrada="10:30")
    a1 = Alumno(id=20, nombre="Marcelo", apellido="Salas", salon=s1)

    db.session.add(s1)
    db.session.add(a1)
    db.session.commit()







if __name__ == "__main__":
    app.run(debug=True)