from flask import Flask, jsonify, render_template
from connect import Connect
import subprocess
import database_utilities as dbu
from random import shuffle


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/random_names', methods=['GET'])
def get_random_names():
    names = dbu.select('postgresql', 'SELECT name FROM name_list')
    name_list = []
    for name in names:
        name_list.append(name['name'])
    shuffle(name_list)
    return render_template('random_names.html', data=[name_list[0]])
    # return name_list[0]
    # return jsonify({'name':name_list[0].strip()})



if __name__ == '__main__':
    app.run()
