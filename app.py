"""Sample flask app with simple version of madlibs."""

from flask import Flask, render_template, request, jsonify
from random import randint

app = Flask(__name__)

@app.route("/")
def homepage():
    # initially, this was just a simple string we returned:
    # return "<html><body<h1>Hi!</h1></body></html>"

    return render_template("homepage.html", 
                           name="Joel", 
                           lucky_num=randint(1, 100),
                           fruits=["apple", "berry", "cherry"])

@app.route("/another")
def some_other_name():
    return "<html><body<h1>Yo!</h1></body></html>"

@app.route("/questions")
def questions():
    return render_template("questions.html")

@app.route("/story", methods=["POST"])
def show_story():
    noun = request.form.get("noun")
    adj = request.form.get("adjective")
    verb = request.form.get("verb")
    noun2 = request.form.get("noun-2")
    return render_template("story.html", 
        noun=noun,
        adjective=adj,
        verb=verb,
        noun2=noun2
    )

# @app.route("/story-as-json")
# def story_as_json():
#     noun = request.args.get("noun")
#     adj = request.args.get("adjective")
#     verb = request.args.get("verb")
#     noun2 = request.args.get("noun-2")
# 
#     story = f"A long time ago, a { noun } decided to { verb } in a { adj } way with { noun2 }."
# 
#     info = {"name": "Joel",
#             "story": story
#     }
# 
#     return jsonify(info)
