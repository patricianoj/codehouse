# codehouse

Hackathon Project for VMware's CodeHouse in Atlanta.

Project: trueMentor.
A website that recommends college students with mentors based on certain preferences. Using cosine similarity of user responses, we match mentees to mentors in the industry. The purpose of this platform is to help people of underrepresented backgrounds in tech find mentors who might relate to their experiences.

To run:
# In Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
FLASK_APP=application.py flask run
