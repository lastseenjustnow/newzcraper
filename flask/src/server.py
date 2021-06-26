from flask import Flask, render_template, request, jsonify
from flask_table import Table, Col

from mongo.MongoToFlask import MongoToFlask

app = Flask(__name__)
mongo_driver = MongoToFlask()


class ResultsTable(Table):
    info = Col('Databases:')


class ResultInfo(object):
    def __init__(self, info):
        self.info = info


class ItemTable(Table):
    url = Col('url')
    category = Col('category')
    context = Col('context')


class Item(object):
    def __init__(self, d):
        self.url = d['url']
        self.category = d['category']
        self.context = d['text']


@app.route("/")
def hello():
    res = ResultsTable([ResultInfo(db) for db in mongo_driver.list_databases()])
    return render_template('index.html', table=res)


@app.route('/search_by_keyword', methods=['GET', 'POST'])
def search_by_keyword():
    keyword = request.form['keyword']
    docs = mongo_driver.search_by_keyword(keyword)

    # Results shall be jsonified, but for now keep it fancy
    table = ItemTable([Item(doc) for doc in docs])

    return render_template('results.html', table=table)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
