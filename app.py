import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for, request, flash, abort
from flask_wtf.csrf import CSRFProtect

from db import execute_one, execute_query, execute_insert

from mysql.connector import Error

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

    nome = ''
    descricao = ''


    if request.method == 'POST':
        nome = request.form.get('nome').strip()
        descricao = request.form.get('descricao').strip()

        try:
            novo_id = execute_insert(
                'INSERT INTO perfis (nome, descricao) VALUES(%s,%s)',
                (nome,descricao)
            )
            flash(f'Perfil {nome} cadastrado com o ID: {novo_id}', 'success')
            return redirect(url_for('listar_perfis'))

        except Error as erro:
            if erro.errno == 1062:
                flash('Já existe um perfil com este nome', 'danger')
            else:
                raise


    return render_template('perfis/perfis-form.html', nome=nome, descricao=descricao)


@app.route('/perfis')
def listar_perfis():
    perfis = execute_query(
        'SELECT id_perfil, nome, descricao, criado_em FROM perfis ORDER BY nome',
        fetch=True
    )

    return render_template('perfis/perfis-listar.html', perfis=perfis)

@app.route('/perfis/<int:id_perfil>/editar', methods=['GET', 'POST'])
def editar_perfil(id_perfil):
    # Buscar os dados com o ID que veio na rota
    perfil = execute_one(
        'SELECT id_perfil, nome, descricao FROM perfis WHERE id_perfil = %s', (id_perfil,),
    )

    if perfil is None:
        abort(404)















































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