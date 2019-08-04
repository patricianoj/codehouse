import numpy as np # for cosine similarity

top_k = 10 # number of top mentors to recommend mentee

# cosine similarity of two vectors
def cos_sim(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    denom = norm_a * norm_b
    if denom = 0:
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
    similarities.sort(key = itemgetter(1), reverse = True)
            return similarities[:top_k]
