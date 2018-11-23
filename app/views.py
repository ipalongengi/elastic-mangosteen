from app import app

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'This is the login page'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return 'This is the signup page'

