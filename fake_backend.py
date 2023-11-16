import logging
from flask import Flask, Response, request
import flask

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s fake backend [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.INFO)

app = Flask("fake backend", template_folder=".")

@app.route("/listing/<listing_id>")
def getListingPage(listing_id):
    return flask.render_template("fake_template.html", listing_name="fake listing")

@app.route("/submit_login", methods=["POST"])
def submitData():
    logging.info(request.json)

    return Response(status=200)

app.run(port=8001)

# </a></li><li><a href="http://localhost:8001/listing/1">fake listing