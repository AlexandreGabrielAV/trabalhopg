import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for, request
from flask_wtf.csrf import CSRFProtect

from db import execute_one

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Liga a proteção CSRF: todo formulário POST do sistema vai precisar do token
CSRFProtect(app)

# ==============================================================================
# PÁGINAS PRINCIPAIS
# ==============================================================================

@app.route('/')
def inicio():

    return render_template('login.html')


# --------------------
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    return render_template('dashboard.html')


# ==============================================================================
# USUÁRIOS
# ==============================================================================


# --------------------
@app.route('/cadastros', methods=['GET', 'POST'])
def inserir_usuarios():

    return render_template('usuarios/usuarios-form.html')


# --------------------
@app.route('/usuarios/listar')
def listar_usuarios():
    
    return render_template('usuarios/usuarios-listar.html')


# ==============================================================================
# FILMES
# ==============================================================================


# --------------------
@app.route('/filmes', methods=['GET', 'POST'])
def inserir_filmes():
    
    return render_template('filmes/filmes-form.html')


# --------------------
@app.route('/listarfilmes', methods=['GET', 'POST'])
def listar_filmes():
    
    return render_template('filmes/filmes-listar.html')


# ==============================================================================
# ALUGUÉIS
# ==============================================================================


@app.route('/aluguel', methods=['GET', 'POST'])
def inserir_aluguel():
    
    return render_template('alugueis/aluguel-form.html')


# --------------------
@app.route('/listaraluguel', methods=['GET', 'POST'])
def listar_aluguel():
    
    return render_template('alugueis/aluguel-listar.html')



# ==============================================================================
# PERFIS
# ==============================================================================


@app.route('/perfis/inserir', methods=['GET', 'POST'])
def inserir_perfil():

    if request.method == 'POST':
        redirect(url_for(listar_perfis))

    return render_template('perfis/perfis-form.html')


@app.route('/perfis/listar')
def listar_perfis():

    return render_template('perfis/perfis-listar.html')


















































# ==============================================================================
# TELAS DE ERROS
# ==============================================================================

@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template('404.html'), 404


@app.errorhandler(500)
def erro_no_servidor(erro):
    return render_template('500.html'), 500


# ==============================================================================
# FINAL
# ==============================================================================


if __name__ == '__main__':
    app.run(debug=True)