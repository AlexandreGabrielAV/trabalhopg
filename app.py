from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = 'appnovo'


@app.route('/')
def inicio():

    return render_template('login.html')




# --------------------
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    return render_template('dashboard.html')




# --------------------
@app.route('/cadastros', methods=['GET', 'POST'])
def inserir_usuarios():

    return render_template('usuarios/usuarios-form.html')


# --------------------
@app.route('/usuarios/listar')
def listar_usuarios():
    
    return render_template('usuarios/usuarios-listar.html')



# --------------------
@app.route('/filmes', methods=['GET', 'POST'])
def inserir_filmes():
    
    return render_template('filmes/cadastrar_filmes.html')


# --------------------
@app.route('/listarfilmes', methods=['GET', 'POST'])
def listar_filmes():
    
    return render_template('filmes/listar_filmes.html')






@app.route('/aluguel', methods=['GET', 'POST'])
def inserir_aluguel():
    
    return render_template('alugueis/aluguel.html')


# --------------------
@app.route('/listaraluguel', methods=['GET', 'POST'])
def listar_aluguel():
    
    return render_template('alugueis/listar_aluguel.html')



if __name__ == '__main__':
    app.run(debug=True)