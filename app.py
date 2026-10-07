from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'appnovo'


LISTA_USUARIOS = []

@app.route('/')
def inicio():
    filmes_destaque = [
        {"titulo": "Inception", "categoria": "Ficção Científica", "imagem": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&auto=format&fit=crop&q=80"},
        {"titulo": "Interstellar", "categoria": "Ficção Científica", "imagem": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=500&auto=format&fit=crop&q=80"},
        {"titulo": "Cinema Paradiso", "categoria": "Drama", "imagem": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=500&auto=format&fit=crop&q=80"},
        {"titulo": "The Dark Knight", "categoria": "Ação", "imagem": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=500&auto=format&fit=crop&q=80"}
    ]
    return render_template('index.html', filmes=filmes_destaque)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Procura o usuário cadastrado na lista
        usuario_encontrado = None
        for u in LISTA_USUARIOS:
            if u['email'] == email and u.get('senha') == senha:
                usuario_encontrado = u
                break

        if usuario_encontrado:
            # Salva na sessão
            session['usuario_logado'] = usuario_encontrado['nome']
            session['nivel_acesso'] = usuario_encontrado['nivel_acesso']

            # Redireciona conforme o nível de acesso
            if usuario_encontrado['nivel_acesso'] == 'Administrador':
                return redirect(url_for('listagem'))
            return redirect(url_for('inicio'))
        else:
            flash('E-mail ou senha incorretos!', 'danger')

    return render_template('login.html')




@app.route('/cadastros', methods=['GET','POST'])
def cadastro():

    if request.method == 'POST':

        nivel = request.form.get('nivel_acesso')

        dados_usuario = {
            'id': len(LISTA_USUARIOS) + 1,
            'nome':request.form.get('nome'),
            'email':request.form.get('email'),
            'celular':request.form.get('celular'),
            'data_nascimento':request.form.get('data_nascimento'),
            'cpf':request.form.get('cpf'),
            'nivel_acesso':request.form.get('nivel_acesso'),
            'categoria_filme':request.form.get('categoria_filme'),
            'idioma_principal':request.form.get('idioma_principal'),
            'cep':request.form.get('cep'),
            'endereco':request.form.get('endereco'),
            'numero':request.form.get('numero'),
            'complemento':request.form.get('complemento'),
            'cidade':request.form.get('cidade'),
            'estado':request.form.get('estado'),
            'senha':request.form.get('senha')
        }


        LISTA_USUARIOS.append(dados_usuario)


        session['usuario_logado'] = dados_usuario['nome']
        session['nivel_acesso'] = nivel

        return redirect(url_for('cadastro'))


    return render_template('cadastros.html')


@app.route('/usuarios', methods=['GET', 'POST'])
def listagem():

    nivel_atual = session.get('nivel_acesso')

    if nivel_atual == 'Administrador':
        return render_template('usuarios.html', usuarios=LISTA_USUARIOS)
    

    return render_template('index.html')




if __name__ == '__main__':
    # Roda o servidor no modo de desenvolvimento (atualiza automático ao salvar)
    app.run(debug=True)