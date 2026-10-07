from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = 'appnovo'


@app.route('/')
def inicio():

    return render_template('index.html')




@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.html')




@app.route('/cadastros', methods=['GET', 'POST'])
def cadastro():

    return render_template('cadastros.html')



@app.route('/usuarios')
def listagem():
    
    return render_template('usuarios.html')




if __name__ == '__main__':
    app.run(debug=True)