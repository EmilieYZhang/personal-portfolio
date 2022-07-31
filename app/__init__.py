import os
import json
import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict
import urllib.request

load_dotenv()  # Loads the environment variables from the .env file

app = Flask(__name__)  # Initializes a Flask app

os.getenv("API_KEY")  # Obtains the value of the .env variable containing the Google Maps API key

# if testing, set db to in-memory sqlite db
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    # Connect to the database using MySQLDatabase function from peewee
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )

print(mydb)

# Adding peewee model that reflects timeline fields
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

# Route for the landing page
@app.route('/')
def index():
    """
    Serves the landing page.
    """
    return render_template('index.html', title="Emilie Zhang", url=os.getenv("URL"))

# Route for the profile page
@app.route('/profile/<name>')
def profile(name):
    """
    Loads profile dynamically from the JSON file and serves profile page.
    
    If profile could not be found, redirects to the landing page.
    """
    data = load_profiles_from_json('data.json')
    if name in data:
        info = data[name]
        return render_template('profile.html', name=name, info=info, url=os.getenv("URL"), API_KEY=os.getenv("API_KEY"))
    else:
        return index()

# Route for timeline post page
@app.route('/timeline')
def timeline():
    post_database = [
        model_to_dict(p)
        for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
    ]
    return render_template('timeline.html', title="Timeline", post_database=post_database)

# Route for handling 404 errors
@app.errorhandler(404)
def not_found(e):
    """
    Redirects any invalid URL to the landing page.
    """
    return render_template("index.html")


def load_profiles_from_json(filename) -> dict:
    """
    Loads profile data by parsing the JSON file provided.

    :param: The JSON file to parse
    :return: A dict containing all the JSON info parsed
    """
    # Get the relative path for the JSON data
    path = f'{os.getcwd()}/{filename}'
    # Open the file and return its parsed contents
    # UTF-8 encoding is used to parse apostrophes correctly
    with open(path, "r", encoding='utf8') as file:
        return json.load(file)

# POST route which adds a timeline post:
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    try: # check if name exists in the request
        name = request.form['name']
    except: # otherwise return 400 status code with message 
        return "Invalid name", 400 
    email = request.form['email']
    content = request.form['content']

    # regex to check for valid email addresses
    check_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(check_email, email):
        return "Invalid email", 400

    if name == "": # check if name is empty first
        return "Invalid name", 400
    elif content == "": # then check content
        return "Invalid content", 400
    else: # add post if both are valid
        timeline_post = TimelinePost.create(name=name, email=email, content=content)
        return model_to_dict(timeline_post)

# GET endpoint to retrieve all timeline posts ordered by created_at descending
# newest timeline posts returned at the top
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

# DELETE endpoint to delete specific posts from timeline
@app.route('/api/timeline_post/<id>', methods=['DELETE'])
def delete_time_line_post(id):
    try:
        post_to_delete = TimelinePost.get(TimelinePost.id == id)
        post_to_delete.delete_instance()
        message="Post deleted\n"
    except:
        message="An error occured when deleting\n"
    return message

@app.route('/health')
def healthcheck():
    # testing the nginx redirection, https redirection
    code = urllib.request.urlopen("https://emilieportfolio.duckdns.org/").getcode()
    print(code)
    if code == 200:
        message="Nginx test: Website up"
    else:
        message="Nginx test: Something is wrong!"
    return message
    # testing mysql container
    # testing myportfolio container


if __name__ == "__main__":
    app.run(debug=True)