from flask import Flask, jsonify, request

from data import all_authors, all_blogs, get_author, get_blog, update_blog

app = Flask(__name__)


@app.route("/")
def route_hello_world():
    return "Hello, World!"


@app.route("/blogs")
def route_all_blogs():
    return jsonify(all_blogs())


@app.route("/blogs/<id>", methods=["GET"])
def route_all_blog(id: str):
    return jsonify(get_blog(int(id)))