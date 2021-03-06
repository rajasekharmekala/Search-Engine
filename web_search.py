# importing Flask and other modules
from curses import flash
from flask import Flask, request, json, render_template
import numpy as np
from search import Search
from time import process_time

retriever = Search()

# Flask constructor
# app = Flask(__name__)
app = Flask(__name__, static_url_path='',  static_folder='web/')
# A decorator used to tell the application
# which URL is associated function
@app.route('/query/<text>', methods=["GET"])
def search(text):
    data = {}
    data["result"] = []
    if request.method == "GET":
        start = process_time()
        results = retriever.search_query(text,5)
        data['time'] = "Query response time in ms: " + str((process_time() - start)*1000)
        data['result'] = results
        # columns = [0, 1, 2, 3, 4]
        # data['result'] =  ["https://canvas.eee.uci.edu/courses/43306", "https://edstem.org/us/courses/16359/discussion/1251389", "https://www.geeksforgeeks.org/how-to-create-dictionary-and-add-key-value-pairs-dynamically/"
        #            , "https://www.igb.uci.edu/~pfbaldi/", "https://panageas.github.io/"]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response



if __name__ == '__main__':
    app.run()