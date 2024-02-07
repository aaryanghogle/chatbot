from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = 'mitali_aaryan_project'  # Replace with your secret key

# Mock user data (replace with your actual authentication logic)
users = {
    'user': 'password',
}


@app.route('/')
def index():
    if 'username' in session:
        # If the user is logged in, redirect to the home page
        return redirect(url_for('home'))
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if users.get(username) == password:
            # Valid login, set the session variable
            session['username'] = username
            return redirect(url_for('home'))
        else:
            # Invalid login, redirect back to the login page with an error message
            return render_template('login.html', error=True)

    return render_template('login.html', error=False)


@app.route('/home')
def home():
    if 'username' in session:
        # Fetch the username from the session
        username = session['username']
        return render_template('homeafterlogin.html', username=username)
    else:
        # If not logged in, redirect to the login page
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # Remove the username from the session
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
