from flask import Flask, render_template
from flask_table import Table, Col

from mongo.hello import list_databases

app = Flask(__name__)


class ResultsTable(Table):
    info = Col('Databases:')


class ResultInfo(object):
    def __init__(self, info):
        self.info = info


@app.route("/")
def hello():
    res = ResultsTable([ResultInfo(db) for db in list_databases()])
    return render_template('index.html', table=res)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
