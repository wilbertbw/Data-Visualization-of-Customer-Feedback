import numpy as np
import matplotlib.pyplot as plt

# aroma votes data, omit the 0 votes
brownie_a_ratings = np.array([4,2,19])
brownie_b_ratings = np.array([2,3,4,4,12])
brownie_c_ratings = np.array([4,3,3,15])
brownie_d_ratings = np.array([4,1,5,4,11])

# set labels for the pie chart, omit the 0 votes
rating_labels_a = ["3 stars", "4 stars", "5 stars"]
rating_labels_b = ["1 star", "2 stars", "3 stars", "4 stars", "5 stars"]
rating_labels_c = ["2 stars", "3 stars", "4 stars", "5 stars"]
rating_labels_d = ["1 star", "2 stars", "3 stars", "4 stars", "5 stars"]


# create function to show value
def make_autopct(ratings):
    def values(pct):
        total = sum(ratings)
        val = int(round(pct * total/100.0))
        if val != 0:
            return '{v:d}\nVotes'.format(v = val)
    return values


plt.figure("Brownie A Aroma Ratings")
plt.pie(brownie_a_ratings, labels = rating_labels_a, autopct = make_autopct(brownie_a_ratings))
plt.title("Brownie A Aroma Ratings")

plt.figure("Brownie B Aroma Ratings")
plt.pie(brownie_b_ratings, labels = rating_labels_b, autopct = make_autopct(brownie_b_ratings))
plt.title("Brownie B Aroma Ratings")

plt.figure("Brownie C Aroma Ratings")
plt.pie(brownie_c_ratings, labels = rating_labels_c, autopct = make_autopct(brownie_c_ratings))
plt.title("Brownie C Aroma Ratings")

plt.figure("Brownie D Aroma Ratings")
plt.pie(brownie_d_ratings, labels = rating_labels_d, autopct = make_autopct(brownie_d_ratings))
plt.title("Brownie D Aroma Ratings")


plt.show()
