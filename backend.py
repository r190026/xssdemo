import logging
from flask import Flask, Response, request
import flask

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s real backend [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.INFO)

app = Flask("demo backend", template_folder=".")

curr_entries = ["real listing 1", "real listing 2"]

@app.route("/entries", methods=["GET"])
def getRoutes():
    response = flask.jsonify(curr_entries)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/listing/<listing_id>")
def getListingPage(listing_id):
    return flask.render_template("real_template.html", listing_name=curr_entries[int(listing_id)])

@app.route("/submitNewListing", methods=["POST"])
def postNewListing():
    curr_entries.append(request.data.decode())
    return Response(status=200)

@app.route("/submit_login", methods=["POST"])
def submitData():
    logging.info(request.json)

    return Response(status=200)


app.run(port=8000)