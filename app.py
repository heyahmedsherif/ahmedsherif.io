from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'more to come very soon on ahmedsherif.io'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)