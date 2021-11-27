# IS A WEB FRAMEWORK
# 
# FIRST SERVER (RUNNING SERVER) ***********
# INSTALLING FLASK:
# Using GitBash - OPEN NEW DIRECTORY(Folder)

# ON WINDOWS - ACTIVATING VIRTURAL ENVIRONMENT
import flask


python -m venv venv

. venv/Scripts/activate

# FLASK INSTALL
pip install flask

# MAKE PYTHON FILE TO WRITE CODE
# app.py - DEFAULT NAME
touch app.py

# IN VSCODE!
# OPEN THE app.py FILE JUST CREATED
# INSTALL FLASK:
from flask import Flask

app = Flask(__name__)

# IN GIT BASH!
# RUN FILE:
flask run
# Ctrl-C to quit

# RUNNING FLASK APP IF FLASK APP FILE ISN'T CALLED app:
FLASK_APP=name_of_app.py flask run



# DEVELOPMENT MODE **************
# MOST PROFESSIONAL CODE IS WRITTEN IN A DEVELOPMENT ENVIRONMENT
# THEN TEST ENVIRONMENT THEN DEPLOYED TO PRODUCTION

# DEVELOPMENT MODE - DEBUG MODE IS ACTIVATED
# Debugger will be shown for "unhandled exceptions", and server will be
# reloaded when code changes.
# IN GIT BASH!
FLASK_ENV=development flask run 

# WHEN A CHANGE IS MADE IN FILE, SERVER AUTOMATICALLY RELOADS

# TO HAVE SERVER AUTOMATICALLY START IN DEVELOPMENT MODE:
# IN GIT BASH!
export FLASK_ENV=development

flask run
# NOTE!!!! - IF TERMINAL IS CLOSED, DEFAULTS BACK TO PRODUCTION!

# CONFIGURE FLASK ENVIRONMENT TO DEFAULT TO DEVELOPMENT MODE ***********
# Go to home directory if not already threre
cd~ or cd .. all the way out

ls -a # To view hidden files
# Look for .bash_profile
open .bash_profile
# ADD TO BASH PROFILE, TYPE:
export FLASK_ENV=development



# ADDING ROUTES ****************

# A function that returns web response is called a "view"
#   Response is a string
#   Usually a string of HTML

# ADD ROUTE - @name of app .route('/path name')
@app.route('/hello')   # This is called a Decorator becuase of the "@"
def say_hello():
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the Home page</p>
            <a href='/hello'>Go to hello page</a>
            <br>
            <a href='/goodbye'>Go to goodbye page</a>
        </body>
    </html>
    """
    return html

@app.route('/hello')
def say_hello():
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the Hello page</p>
        </body>
    </html>
    """
    return html

@app.route('/goodbye')
def say_bye():
    return "GOODBYE!!!"
# ^^^^ - THese routes are all GET requests



# QUERY STRING PARAMETERS *************
# "request" - Built in object, represents web requests
@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results For: {term}</h1> <p>Sorting by: {sort}</p>"
# 127.0.0.1:5000/searc?term=Dogs&sort=New



# POST REQUESTS *************
# By default, a route only responds to GET requests
# Must specify to accept POST requests
@app.route("/my/route", methods=["POST"])
def handle_post_to_my_route():
    ...

#GIT BASH
curl -X POST http://127.0.0.1:5000/post

@app.route("/post", methods=["POST"])
def post_demo():
    return "YOU MADE A POST REQUEST!"


@app.route("/add-comment")
def add_comment_form():
    return """
        <h1>Add Comment</h1>
        <form method="POST">
            <input type='text' placeholder='comment' name='comment'/>
            <input type='text' placeholder='username' name='username'/>
            <button>Submit</button>
        </form>
    """


@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment=request.form["comment"]
    username = request.form["username"]
    print(request.form)
    return f"""
    <h1>SAVED YOUR COMMENT</h1>
    <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</ul>
    </ul>
    """



# Path Variables **********
#Extracting data from a URL and using that data to create dynamic routes
@app.route('/r/<subreddit>') # Wrapping in <> turns into variable subreddit
def show_subreddit():
    return "THIS IS A SUBREDDIT"

@app.route('/r/<subreddit>') 
def show_subreddit(subreddit): #NEEDS TO MATCH APP ROUTE. Ex: subreddit
    return f"<h1>Browsing the {subreddit} Subreddit</h1>"
# <variable_name> in @app.route
# View function must have same "var_name" as parameter

USERS = {
    "whiskey": "Whiskey the dog",
    "spike": "Spike the porcupine",
    "sadie": "Sadie the dog",
}

@app.route('/user/<username>')
def show_user_profile(username):

    name = USERS.get(username, "Username not found")
    return f"<h1>Profile for <br>{name}</h1>"

POSTS = {
    1: "I like chicken tenders",
    2: "I hate mondays",
    3: "Double rainbow!",
}

@app.route('/posts/<int:id>')
def show_posts(id):
    post = POSTS.get(id, "Post not found")
    return f"<h1>{post}</h1>"
#python only recognizes keys as strings. Ex. /posts/2 it sees as '2'
# <int:id> will allow python to read key as integer



# MORE ON ROUTE PARAMETERS *****************
# Can have multiple variables
# Example:
PRODUCT = {
    apple: "Fruit",
    banana: "Fruit",
    Onion: "Vegetable"
}

@app.route("/products/<category>/<product_id>")
def product_detail(category, product_id):
#     """Show detial page for product"""
    produce = PRODUCT[category, product_id]
    return f"<h1>Viewing description for produce {product_id} in the {category} category</h1>"

#QUERY PARAMS(query strings) VS URL PARAMS(Route variables)
# http://toys.com/shop/spinning-top?color=red
# /shop/spinning-top is the ROUTE VARIABLE
# color=red is the query string

# URL PARAMETER:
# /shop/<toy>
# More like "subject of page"

# QUERY PARAMETER:
# /shop?toy=elmo
# More like "extra info about page"
# Often used when coming from form








































































































































































