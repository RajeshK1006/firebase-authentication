from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase
import re
import urllib.parse

app = Flask(__name__)
app.secret_key = "YourSecretKey"

# Initialize Firebase

firebaseConfig = {
    'apiKey': "YOURAPIKEY",
    'authDomain': "YOUR-PROJECT-DOMAIN-AUTH",
    'projectId': "YOUR-PROJECT-ID",
    'storageBucket': "YOUR-PROJECT-STRAGE-BUCKET",
    'messagingSenderId': "MESSAGING-id",
    'appId': "YOUR-WEB-APP-ID",
    'measurementId': "YOUR-MEASUREMENT-ID",
    'databaseURL': "YOUR-REALTIME-DATABSE-URL"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# Email validation function
def is_valid_email(email):
    # Use regular expression to validate email format
    return re.match(r"[^@]+@srmist\.edu\.in", email)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        register_number = request.form['register_number']
        phone_number = request.form['phone_number']
        
        if not is_valid_email(email):
            return "Please use your SRMIST email for sign Up"
        

        
        try:
            encoded = urllib.parse.quote(email,safe="")
            
            users = db.child('users').get()
            if users.each():
                for user in users.each():
                    user_data = user.val()
                    if user_data.get('email') == email:
                        return "This email is already signed up. Please go back to the login page."
            
        except Exception as e:
            return str(e)
            
        
        
        try:
            
            user = auth.create_user_with_email_and_password(email, password)
            uid = user['localId']

            user_data = {
                'name': name,
                'register_number': register_number,
                'phone_number': phone_number,
                'email':email
            }
            db.child('users').child(uid).set(user_data)

            return redirect(url_for('login'))
        except Exception as e:
            return render_template('signup.html', error=str(e))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            return redirect(url_for('dashboard'))
        except Exception as e:
            return render_template('login.html', error=str(e))

    return render_template('login.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        try:
            auth.send_password_reset_email(email)
            return "Password reset email sent. Please check your email."
        except Exception as e:
            return "An error occurred: " + str(e)
    return render_template('forget.html')

# @app.route('/reset_password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
#     if request.method == 'POST':
#         new_password = request.form['new_password']
#         confirm_password = request.form['confirm_password']

#         # Validate passwords
#         if new_password != confirm_password:
#             return "Passwords do not match. Please try again."

#         try:
#             # Reset password using the token
#             auth.confirm_password_reset(token, new_password)
#             return "Password updated successfully."
#         except Exception as e:
#             return "An error occurred: " + str(e)

#     # Render the reset password page
#     return render_template('reset_password.html')


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        user = session['user']
        # You can retrieve user data from Firebase and pass it to the template
        return render_template('dashboard.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/logout', methods = ["POST","GET"])
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
