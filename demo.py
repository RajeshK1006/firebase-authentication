import pyrebase
# Initialize Firebase
firebaseConfig = {
    'apiKey': "AIzaSyAqJdMG-Txy9T6ZBM8st9v0zOLSbj_s4YM",
    'authDomain': "demodata-f30d4.firebaseapp.com",
    'projectId': "demodata-f30d4",
    'storageBucket': "demodata-f30d4.appspot.com",
    'messagingSenderId': "46300493327",
    'appId': "1:46300493327:web:632fefe1be5a12a51a957a",
    'measurementId': "G-1P90QHKWPJ",
    'databaseURL': "https://demodata-f30d4-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

def signup():
    email = input("enter the email: ")
    pasword = input("enter the password: ")
    user = auth.create_user_with_email_and_password(email,pasword)
    return 

def check():
    ans = input("are you an new user: y/n")
    if ans == "y":
        return signup()

check()