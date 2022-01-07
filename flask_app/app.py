from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

server = Flask(__name__)
es = Elasticsearch('elasticsearch', port=9200, http_auth=('elastic', 'changeme'))



@server.route('/')
def home():
    return render_template('search.html')

@server.route('/search/', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    res = [] #modify using the elasticsearch api
    return render_template('results.html', res=res )
