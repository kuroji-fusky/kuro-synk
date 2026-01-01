from argparse import ArgumentParser
from flask import Flask, render_template, make_response

parser = ArgumentParser()

parser.add_argument("--dev", action="store_true",
                    help="Enable hot reload and stuff")

args = parser.parse_args()

kapp = Flask(__name__)


@kapp.after_request
def resp_hook(resp):
    resp.headers["X-Robots-Tag"] = "noindex"

    return resp


@kapp.route("/")
def home_sweet_home():
    return render_template("index.html")


@kapp.route("/commits")
def commit_page():
    return render_template("commits.html")


if __name__ == "__main__":
    kapp.run(host="127.0.0.1", port=8080, debug=bool(args.dev))
