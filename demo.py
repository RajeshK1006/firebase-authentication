import pyrebase
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