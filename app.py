from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []
posts = []

@app.route('/')
def home():
    return render_template('posts.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users.append({'username': username, 'password': password})
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and user['password'] == password:
                return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/post', methods=['POST'])
def post():
    content = request.form['content']
    posts.append(content)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
