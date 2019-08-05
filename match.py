import numpy as np # for cosine similarity
import operator

top_k = 3 # number of top mentors to recommend mentee

# cosine similarity of two vectors
def cos_sim(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    denom = norm_a * norm_b
    if denom == 0:
        return 0
    return dot_product / denom

# gets top mentors based on similarities
# param mentee: vector of mentor preferences
# param mentors: array of mentors [id, [vector of information]]
def get_recommendations(mentee, mentors):
    similarities = [] # [[id1, similaritiy1], [id2, similaritiy2]...]
    for i in range(len(mentors)):
        similarity = cos_sim(mentee, mentors[i][1])
        similarities.append([mentors[i][0], similarity])
    similarities.sort(key = operator.itemgetter(1), reverse = True)
    print(similarities)
    return similarities[:top_k]

# [name,[Latinx, Black, AmericanIndian, Womyn, LGBTQ+, Introvert (1-5), Imposter, Art, Dance, Sports, Outdoors, Travel, VideoGames, Experience (1-4), Rural, Urban, Suburban]]
mentors = [["Patricia", [1,0,0,1,1,5,1,0,0,1,1,1,0,2,1,0,0]], ["Lucerito", [1,0,0,0,0,4,1,0,1,0,0,1,0,3,1,0,1]], ["Leroy", [0,0,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0]],["Shikiko", [0,1,0,0,1,2,1,1,1,0,0,0,0,2,1,0,0]], ["Mia", [1,0,0,1,1,5,1,0,0,1,1,1,0,2,1,0,0]]] 

mentee = [1,0,0,0,1,4,0,0,0,1,1,1,0,2,1,0,0]

get_recommendations(mentee, mentors)
