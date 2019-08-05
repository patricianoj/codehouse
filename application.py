from flask import Flask
app = Flask(__name__)

import json
from flask import Flask, request, redirect, g, render_template
import requests
from urllib.parse import quote
import match
from firebase import Firebase

config = {
    "apiKey": "AIzaSyCWjG4iohkqyi8PmfxRSeZrnlO9aKwPzjU",
    "authDomain": "codehouse-dcc1a.firebaseapp.com",
    "databaseURL": "https://codehouse-dcc1a.firebaseio.com",
    "projectId": "codehouse-dcc1a",
    "storageBucket": "codehouse-dcc1a.appspot.com",
    "messagingSenderId": "121564344566",
    "appId": "1:121564344566:web:a869a5a99a92dc9f"
}

firebase = Firebase(config)
db = firebase.database()

@app.route("/")
def index():
    # get the value of user id from query parameter (i.e. ?user_id=some-value)
    id = request.args.get('user_id')
    print(id)
    return render_template("index.html", user_id=id)

@app.route("/api/post/mentor_preferences", methods = ['POST'])
def set_mentor_request():
    # get the value of user id from query parameter (i.e. ?user_id=some-value)
    id = request.args.get('user_id')
    print(id)
    
    # get form values
    '''
        Form structure:
        checkboxes: Latinx, Black, AmericanIndian, Womyn, LGBTQ
        radio: Introvert (1-5)
        radio: Imposter
        checkboxes: Dance, Sports, Outdoors, Travel, VideoGames
        dropdown: Experience (1, 2, 3, 4)
        checkboxes: grewUp - Rural, Urban, Suburban
    '''
    print(request.form.get('Latinx'))
    
    # create vector of preferences
    vector = [request.form.get('Latinx'),
              request.form.get('Black'),
              request.form.get('AmericanIndian'),
              request.form.get('Womyn'),
              request.form.get('LGBTQ'),
              request.form.get('Introvert'),
              request.form.get('Imposter'),
              request.form.get('Art'),
              request.form.get('Dance'),
              request.form.get('Sports'),
              request.form.get('outdoors'),
              request.form.get('Travel'),
              request.form.get('VideoGames'),
              request.form.get('experience'),
              request.form.get('grewUp'),
              request.form.get('grewUp2'),
              request.form.get('grewUp3')]
    
    print(vector)
    
    # store vector in database
    mentee_vector = {"vector": str(vector)}
    db.child("users").child("mentees").child("mentees").child(id).set(mentee_vector)
    # TO DO: handle update case
    
    # set mentor preferences from database
    mentor_vectors = []
    mentor_vectors = get_mentor_info()
    
    # calculate similarities and return most similar
    recommendations = match.get_recommendations(mentee, mentor_vectors)
    print(recommendations)
    
    return render_template("recommendations.html", recommendations)

def get_mentor_info():
    # get vectors for all mentors
    mentor_vectors = []
    all_mentors = db.child("users").child("mentors").child("mentors").get()
    for mentor in all_mentors.each():
        mentor_vectors.append(mentor.child("vector").get().val())

if __name__ == "__main__":
    app.run(debug=True, port=PORT)	
 	
