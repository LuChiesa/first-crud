import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)



mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Familiachiesa1@',
    database='database',
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    cursor = mydb.cursor()
    name = request.form['name']
    valor = request.form['valor']
    sql = "INSERT INTO vendas (venda_coluna, valor) VALUES (%s, %s)"
    val = (name, valor)
    cursor.execute(sql, val)
    mydb.commit()
    return 'User created successfully'

@app.route('/read')
def read():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM vendas")
    users = cursor.fetchall()
    return render_template('read.html', users=users)

@app.route('/update/<int:idvendas>', methods=['GET', 'POST'])
def update(idvendas):
    if request.method == 'POST':
        cursor = mydb.cursor()
        name = request.form['name']
        valor = request.form['valor']
        sql = "UPDATE vendas SET venda_coluna = %s, valor = %s WHERE idvendas = %s"
        val = (name, valor, idvendas)
        cursor.execute(sql, val)
        mydb.commit()
        return 'User updated successfully'
    else:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM vendas WHERE idvendas = %s", (idvendas,))
        user = cursor.fetchone()
        return render_template('update.html', user=user)


@app.route('/delete/<int:idvendas>')
def delete(idvendas):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM vendas WHERE idvendas = %s", (idvendas,))
    mydb.commit()
    return 'User deleted successfully'

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)