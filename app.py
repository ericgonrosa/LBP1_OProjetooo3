from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'sua_secret_key'

users = {'usuario': 'senha'}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        session['username'] = username
        session.permanent = True
        flash('Login bem-sucedido!')
        return redirect(url_for('dashboard'))
    else:
        flash('Nome de usuário ou senha incorretos.')
        return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Você precisa estar logado para acessar esta página.')
        return redirect(url_for('home'))
    return f'Olá, {session["username"]}! Bem-vindo ao painel.'

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Você saiu com sucesso.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
