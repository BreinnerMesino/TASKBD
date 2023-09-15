from flask import Flask, render_template, request, redirect, url_for
import pyodbc
#Conexión a base de datos ----------------------------------------------
# Código para correr el servidor con el index de HTML.
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\brein\Documents\Codes\TaskBD\src\TASKBD.accdb")
#Se crea el cursor y se hace una consulta para pedir los datos
cursor = conn.cursor()
#Definir los titulos de cada columna de la lista
headings_Task = ("ID", "Descripción", "Estado")
#Rutas -----------------------------------------------------------------
#Index.
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
#Ruta para leer las tareas.
@app.route('/show-task')
def showTask():
    cursor.execute("SELECT * FROM Tareas") 
    data_Task=cursor.fetchall()
    return render_template('showTask.html', headings=headings_Task, data=data_Task)
#Ruta para agregar una nueva tarea.
@app.route('/new-task')
def newTask(): 
    return render_template('newTask.html')
#Ruta para marcar una tarea como completada
@app.route('/complete-task')
def completeTask():
    return render_template('completeTask.html')
#Ruta para eliminar una tarea
@app.route('/delete-task')
def deleteTask():
    return render_template('deleteTask.html')
if __name__ == '__main__':
    app.run()

cursor.close()
conn.close()