# -------------------------------------------------------------------------
# AUTHOR: Weisheng (Max) Zhang
# FILENAME: similarity.py
# SPECIFICATION: output the two most similar documents according to their cosine similarity
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: approximately an hour (including setting up anaconda)
# -----------------------------------------------------------*/

# Importing some Python libraries
from re import L
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Defining the documents
doc1 = "Soccer is my favorite sport"
doc2 = "I like sports and my favorite one is soccer"
doc3 = "I support soccer at the olympic games"
doc4 = "I do like soccer, my favorite sport in the olympic games"

# Use the following words as terms to create your document matrix
# [soccer, my, favorite, sport, I, like, one, support, olympic, games]
# --> Add your Python code here
vectors = []
features = ["soccer", "my", "favorite", "sport", "i", "like", "one", "support", "olympic", "games"]
doc4 = doc4.replace(',', '')
docs = [doc1.lower(), doc2.lower(), doc3.lower(), doc4.lower()]
for doc in docs:
    vector = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(doc.split())):
        word = doc.split()[i]
        if word in features:
            vector[features.index(word)] = 1
    vectors.append(vector)
vector = np.array(vectors)
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors only
# Use cosine_similarity([X, Y, Z]) to calculate the pairwise similarities between multiple vectors
# --> Add your Python code here
similarity = cosine_similarity(vector)
mostSimilar, first, second = 0, 0, 0
for i in range(len(similarity)):
    for j in range(i+1, len(similarity[0])):
        if i != j and similarity[i][j] > mostSimilar:
            mostSimilar = similarity[i][j]
            first = i+1
            second = j+1
# Print the highest cosine similarity following the template below
# The most similar documents are: doc1 and doc2 with cosine similarity = x
# --> Add your Python code here
print("The most similar documents are: doc" + str(first) + " and doc" + str(second) + " with cosine similarity = " + str(mostSimilar))
# Compare the pairwise cosine similarities and store the highest one