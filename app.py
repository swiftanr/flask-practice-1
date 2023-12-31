import json

from flask import Flask, request

app = Flask(__name__)

posts = [
    {
        "id": 0,
        "upvotes": 1,
        "title": "My cat is the cutest!",
        "link": "https://i.imgur.com/jseZqNK.jpg",
        "username": "alicia98",
    },
    {
        "id": 1,
        "upvotes": 3,
        "title": "Cat loaf",
        "link": "https://i.imgur.com/TJ46wX4.jpg",
        "username": "alicia98",
    },
]
count_posts = 2


@app.route("/")
@app.route("/index")
def index():
    return "Hello World! This is home page ❤️"


@app.route("/api/posts")
def get_posts():
    return json.dumps({"posts": posts}), 200


@app.route("/api/posts", methods=["POST"])
def add_post():
    title = request.args.get("title")
    link = request.args.get("link")
    username = request.args.get("username")
    if title is None or link is None or username is None:
        return json.dumps({"Error": "Field(s) missing. Bad Request"}), 400
    global count_posts
    id = count_posts + 1
    count_posts += 1
    post = {
        "id": id,
        "upvotes": 1,
        "title": title.replace("-", " "),
        "link": link,
        "username": username
    }
    posts.append(post)

    return json.dumps({"posts": posts}), 201


if __name__ == "__main__":
    app.run(debug=True)
