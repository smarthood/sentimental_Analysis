import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
# Fetch the service account key JSON file contents
cred = credentials.Certificate('path/to/serviceAccountKey.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)
# Get the user input
email = input("Enter email: ")
password = input("Enter password: ")
# Try to sign in the user with the provided email and password
try:
    user = auth.authenticate(email=email, password=password)
    print("Successfully signed in as user with uid:", user.uid)
except auth.InvalidEmailError:
    print("Invalid email provided")
except auth.WrongPasswordError:
    print("Wrong password provided")
except auth.UserNotFoundError:
    print("User with provided email not found")
