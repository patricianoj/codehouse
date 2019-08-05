from flask import Flask
app = Flask(__name__)

import yaml
import json
from flask import Flask, request, redirect, g, render_template
import requests
from urllib.parse import quote
import match
# from firebase import Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

config = {
    "apiKey": "AIzaSyCWjG4iohkqyi8PmfxRSeZrnlO9aKwPzjU",
    "authDomain": "codehouse-dcc1a.firebaseapp.com",
    "databaseURL": "https://codehouse-dcc1a.firebaseio.com",
    "projectId": "codehouse-dcc1a",
    "storageBucket": "codehouse-dcc1a.appspot.com",
    "messagingSenderId": "121564344566",
    "appId": "1:121564344566:web:a869a5a99a92dc9f"
}

cred = credentials.Certificate("codehouse-dcc1a-91e6d1af0fce.json")
default_app = firebase_admin.initialize_app(cred, options=config)
root = db.reference()

@app.route("/")
def index():
    # get the value of user id from query parameter (i.e. ?user_id=some-value)
    user_id = request.args.get('id')
    print(user_id)
    return render_template("index.html", name=user_id)

@app.route("/api/post/mentor_preferences", methods = ['POST'])
def set_mentor_request():
    # get the value of user id from query parameter (i.e. ?user_id=some-value)
    id = request.args.get('id')
    print(id)
    print(root.get())    
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

    v = []
    for entry in vector:
        if entry == 'on':
            v.append(1)
        elif type(entry) == str:
            v.append(int(entry)) 
        #if entry.isdigit()
        #     v.append(int(entry))
	# == None:
        #if entry == 'on':
        #    v.append(1)
        else:
            v.append(0)  
    
    print(v)
  
    print(id)  
    # store vector in database
    mentee_vector = {"vector": str(v)}
    root.child("users").child("mentees").child("mentees").child(id).set(mentee_vector)
    # TO DO: handle update case

    # store vector in database
    mentee_vector = {"vector": str([1,0,0,1,1,5,1,0,0,1,1,1,0,2,1,0,0])}
    root.child("users").child("mentors").child("mentors").child("Laura").set(mentee_vector)
    
    # store vector in database
    mentee_vector = {"vector": str([1,0,0,0,0,4,1,0,1,0,0,1,0,3,1,0,1])}
    root.child("users").child("mentors").child("mentors").child("Lucerito").set(mentee_vector)

    # store vector in database
    mentee_vector = {"vector": str([0,0,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0])}
    root.child("users").child("mentors").child("mentors").child("Leroy").set(mentee_vector)

    # store vector in database
    mentee_vector = {"vector": str([0,1,0,0,1,2,1,1,1,0,0,0,0,2,1,0,0])}
    root.child("users").child("mentors").child("mentors").child("Shikiko").set(mentee_vector)
    
    # store vector in database
    mentee_vector = {"vector": str([1,0,0,1,1,5,1,0,0,1,1,1,0,2,1,0,0])}
    root.child("users").child("mentors").child("mentors").child("Mia").set(mentee_vector)

    # set mentor preferences from database
    mentor_vectors = []
    mentor_vectors = get_mentor_info()
    
    # calculate similarities and return most similar
    recommendations = match.get_recommendations(v, mentor_vectors)
    print(recommendations)
    
    return render_template("recommendations.html", mentors=recommendations)

def get_mentor_info():
    # get vectors for all mentors
    mentors= []
    mentor_vectors = []
    print(root.get())
    all_mentors = root.child("users").child("mentors").child("mentors").get()
    print(all_mentors)
    for mentor in all_mentors:
        m = all_mentors.get(str(mentor)).get("vector")
        m = m.replace('[','')
        m = m.replace(']','')
        m = [int(i) for i in m.split(',')]
        mentor_vectors.append(m)
        mentors.append([mentor,m])
    print(mentors)
    return mentors

if __name__ == "__main__":
    app.run(debug=True, port=PORT)	
