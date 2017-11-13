"""
Simple User Interface
"""
from movielens import *
from sklearn.cluster import KMeans

import numpy as np
import pickle
import random
import sys
import time

def recommend():
    user = []
    item = []

    d = Dataset()
    d.load_users("data/u.user", user)
    d.load_items("data/u.item", item)

    n_users = len(user)
    n_items = len(item)
    ask = [item[0],item[1],item[23],item[50],item[56],item[63],item[68],item[81],item[88],item[97],item[120],item[132],item[176],item[203],item[225],item[229],item[300],item[365]]
  
    

    utility_matrix = pickle.load( open("utility_matrix.pkl", "rb") )

    # Find the average rating for each user and stores it in the user's object
    for i in range(0, n_users):
        x = utility_matrix[i]
        user[i].avg_r = sum(a for a in x if a > 0) / sum(a > 0 for a in x)

    # Find the Pearson Correlation Similarity Measure between two users
    def pcs(x, y, ut):
        num = 0
        den1 = 0
        den2 = 0
        A = ut[x - 1]
        B = ut[y - 1]
        num = sum((a - user[x - 1].avg_r) * (b - user[y - 1].avg_r) for a, b in zip(A, B) if a > 0 and b > 0)
        den1 = sum((a - user[x - 1].avg_r) ** 2 for a in A if a > 0)
        den2 = sum((b - user[y - 1].avg_r) ** 2 for b in B if b > 0)
        den = (den1 ** 0.5) * (den2 ** 0.5)
        if den == 0:
            return 0
        else:
            return num / den

    # Perform clustering on items
    
    movie_genre = []
    for movie in item:
        movie_genre.append([movie.unknown, movie.action, movie.adventure, movie.animation, movie.childrens, movie.comedy,
                            movie.crime, movie.documentary, movie.drama, movie.fantasy, movie.film_noir, movie.horror,
                            movie.musical, movie.mystery, movie.romance, movie.sci_fi, movie.thriller, movie.war, movie.western])

    movie_genre = np.array(movie_genre)
    cluster = KMeans(n_clusters=19)
    cluster.fit_predict(movie_genre)

    new_user = np.zeros(19)
    for x in ask:
        print(x.title)
    fp = open("ratings.txt","r+")
    l = fp.read()
    fp.close()
    print(l)
    l1 = l.split(',')
    print(l1)
    for movie,a in zip(ask,l1):
	    if new_user[cluster.labels_[movie.id - 1]] != 0:
		    new_user[cluster.labels_[movie.id - 1]] = (new_user[cluster.labels_[movie.id - 1]] + int(a)) / 2
	    else:
		    new_user[cluster.labels_[movie.id - 1]] = int(a)

    utility_new = np.vstack((utility_matrix, new_user))
    user.append(User(944, 21, 'M', 'student', 110018))
    fp.close()

    pcs_matrix = np.zeros(n_users)

    for i in range(0, n_users + 1):
        if i != 943:
            pcs_matrix[i] = pcs(944, i + 1, utility_new)

    user_index = []
    for i in user:
	    user_index.append(i.id - 1)
    user_index = user_index[:943]
    user_index = np.array(user_index)

    top_5 = [x for (y,x) in sorted(zip(pcs_matrix, user_index), key=lambda pair: pair[0], reverse=True)]
    top_5 = top_5[:5]

    top_5_genre = []

    for i in range(0, 5):
	    maxi = 0
	    maxe = 0
	    for j in range(0, 19):
		    if maxe < utility_matrix[top_5[i]][j]:
			    maxe = utility_matrix[top_5[i]][j]
			    maxi = j
	    top_5_genre.append(maxi)
    print(top_5_genre)
    fk = open("predictions.txt","w+")
    fk.write(','.join(str(x) for x in top_5_genre))
    fk.close()
