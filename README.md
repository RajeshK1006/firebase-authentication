# User Authentication with Flask and Firebase

## Overview

This project is a web application built with Python and Flask, integrating Firebase Authentication for user authentication. It allows users to sign up, log in, and access a dashboard after authentication. Pyrebase library is used to interact with Firebase services.

## Features

- **User Authentication**: Users can sign up and log in securely using Firebase Authentication.
- **Dashboard Access**: Authenticated users can access a personalized dashboard.
- **Password Reset**: Forgot password functionality with password reset email sent via Firebase.

## Requirements

- Python 3.9
- Pyrebase4 (`pip install pyrebase4`)
- Flask (`pip install flask`)

## Setting Up Firebase

1. Go to [Firebase Console](https://console.firebase.google.com) and sign in or register for an account.
2. Create a new project and configure it according to your needs.
3. Enable Firebase Authentication and choose the sign-in methods (email/password).
4. Create a Firebase web app and copy the configuration keys.
5. Paste the configuration keys into your Flask app's configuration file (`app.py`).

## Installation

Clone this repository to your local machine:

-git clone "RepositoryURL"

## Install the required Python packages:

-pip install -r requirements.txt

## Usage
-Run the Flask application:

- flask run

-Access the application in your web browser at 'http://localhost:5000'.

## Contributing
-Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or fixes.
