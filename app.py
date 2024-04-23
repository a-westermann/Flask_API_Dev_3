from flask import Flask
import subprocess
import psycopg2

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello World!'




if __name__ == '__main__':
    app.run()
