from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = 'appnovo'


@app.route('/')
def inicio():

    return render_template('index.html')



# --------------------
@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.html')



# --------------------
@app.route('/cadastros', methods=['GET', 'POST'])
def cadastro():

    return render_template('cadastros.html')


# --------------------
@app.route('/usuarios')
def listagem():
    
    return render_template('usuarios.html')



# --------------------
@app.route('/filmes', methods=['GET', 'POST'])
def filmes():
    
    return render_template('filmes.html')


# --------------------
@app.route('/listarfilmes', methods=['GET', 'POST'])
def listar_filmes():
    
    return render_template('listar_filmes.html')






@app.route('/aluguel', methods=['GET', 'POST'])
def aluguel():
    
    return render_template('aluguel.html')


# --------------------
@app.route('/listaraluguel', methods=['GET', 'POST'])
def listar_aluguel():
    
    return render_template('listar_aluguel.html')



if __name__ == '__main__':
    app.run(debug=True)