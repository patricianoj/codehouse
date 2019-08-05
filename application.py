from flask import Flask
app = Flask(__name__)

import json
from flask import Flask, request, redirect, g, render_template
import requests
from urllib.parse import quote
from match import get_recommendations
from firebase import Firebase

db = firebase.database()


@app.route("/")
def index():
    return render_template(index)

@app.route("api/post/mentor_preferences", methods = ['POST'])
def set_mentor_request():
    # get the value of user id from query parameter (i.e. ?user_id=some-value)
    id = request.args.get('user_id')
    
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
    
    # create vector of preferences
    vector = [int(request.form.get('Latinx')),
              int(request.form.get('Black')),
              int(request.form.get('AmericanIndian')),
              int(request.form.get('Womyn')),
              int(request.form.get('LGBTQ')),
              request.form.get('Introvert'),
              request.form.get('Imposter'),
              int(request.form.get('Art')),
              int(request.form.get('Dance')),
              int(request.form.get('Sports')),
              int(request.form.get('outdoors')),
              int(request.form.get('Travel')),
              int(request.form.get('VideoGames')),
              request.form.get('experience'),
              int(request.form.get('outdoors')),
              int(request.form.get('Travel')),
              int(request.form.get('VideoGames')),
              int(request.form.get('grewUp')),
              int(request.form.get('grewUp2')),
              int(request.form.get('grewUp3'))]
    
    print(vector)
    
    # store vector in database
    mentee_vector = {"vector": str(vector)}
    db.child("users").child("mentees").child(user_id).set(mentee_vector)
    # TO DO: handle update case
    
    # set mentor preferences from database
    mentor_vectors = []
    mentor_vectors = get_mentor_info()
    
    # calculate similarities and return most similar
    recommendations = get_recommendations(mentee, mentor_vectors)
    print(recommendations)
    
    return render_template("recommendations.html", recommendations)

def get_mentor_info():
    # get vectors for all mentors
    mentor_vectors = []
    all_mentors = db.child("users").child("mentors").get()
    for mentor in all_mentors.each():
        mentor_vectors.append(mentor.child("vector").get().val())

if __name__ == "__main__":
    app.run(debug=True, port=PORT)	
 	
