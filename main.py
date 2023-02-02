from flask import Flask
from auth import auth
from player import player

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(player)

if __name__ == '__main__':
    from waitress import serve

    # app.run(host='0.0.0.0', debug=True)
    serve(app, host='0.0.0.0', port=5000)
