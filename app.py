import pyotp
from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

users_db = {}

class User(UserMixin):
    def __init__(self, id, username, password, otp_secret=None):
        self.id = id
        self.username = username
        self.password = password
        self.otp_secret = otp_secret if otp_secret else pyotp.random_base32()

# Usuário de exemplo
users_db['testuser'] = User(id=1, username='testuser', password='password123')

def generate_otp_url(user):
    totp = pyotp.TOTP(user.otp_secret)
    return totp.provisioning_uri(name=user.username, issuer_name="MyApp")


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_db.get(username)

        if user and user.password == password:
            login_user(user)
            return redirect(url_for('verify_mfa'))

    return render_template('login.html')

@app.route('/verify_mfa', methods=['GET', 'POST'])
@login_required
def verify_mfa():
    user = current_user
    if request.method == 'POST':
        otp = request.form['otp']
        totp = pyotp.TOTP(user.otp_secret)

        if totp.verify(otp): 
            return redirect(url_for('protected'))
        else:
            return 'Código inválido. Tente novamente.', 400

    otp_url = generate_otp_url(user)
    return render_template('verify_mfa.html', otp_url=otp_url)

@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html', username=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@login_manager.user_loader
def load_user(user_id):
    for user in users_db.values():
        if user.id == int(user_id):
            return user
    return None

if __name__ == '__main__':
    app.run(debug=True)
