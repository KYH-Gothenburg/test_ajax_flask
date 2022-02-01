import json
import random
from flask import Flask, Response, render_template
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)


counter = 1

@app.get('/data')
@cross_origin()
def data():
    global counter
    data_dict = {
        'counter': counter
    }
    counter += 1
    return Response(json.dumps(data_dict), 200, content_type='application/json')


@app.get('/check_message')
@cross_origin()
def check_message():
    # Simulate that we check the db for new messages
    # We want to return a count of the number of new, unread messages
    num_new_msgs = random.randrange(0, 3)
    messages = {
        'numNewMessages': num_new_msgs
    }
    return Response(json.dumps(messages), 200, content_type='application/json')


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/contact')
def contact():
    return render_template('contact.html')


@app.get('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()