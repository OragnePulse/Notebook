 from flask import Flask
app  = Flask (__name__)

@app.route('/')
def home():
    return "Homepage<h1>Welcome to the Homepage</h1>"
if __name__=='_main_':
    app.run(debug=True)
