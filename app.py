import pandas as pd 
import numpy as np
from numpy.linalg import norm

# Load datasets
data = pd.read_csv('PATH_TO_Books Data.csv')
vectors = pd.read_csv('PATH_TO_Recommendation Vectors.csv', index_col='id')

# Function to find the most similar books based on cosine similarity
def more_similar_books(id1):
    # Dictionary to store book titles, cosine similarity values, and book ids
    possible_matches = {'book': [], 'cosine similarity': [], 'id': []}
    
    # Loop through all books in the dataset to compare cosine similarity with the given book (id1)
    for i in range(len(data)):
        id2 = data.iloc[i]['id']
        
        # Skip comparing the book to itself (id1 with id2)
        if id2 == id1:
            continue
        
        # Fetch the feature vectors for both books (ensure they are numerical vectors)
        A = vectors.loc[id1]  # Feature vector for the given book (id1)
        B = vectors.loc[id2]  # Feature vector for another book (id2)
        
        # Calculate cosine similarity between the two vectors
        cosine = np.dot(A, B) / (norm(A) * norm(B))
        
        # If cosine similarity is above a threshold (0.50), store the match details
        if (cosine >= 0.50 and cosine < 0.98):
            possible_matches['book'].append(data.loc[data['id'] == id2]['title'].values[0])
            possible_matches['cosine similarity'].append(cosine)
            possible_matches['id'].append(data.loc[data['id'] == id2]['id'].values[0])
    
    # Create pairs of book titles, cosine similarities, and ids
    pairs = list(zip(possible_matches['book'], possible_matches['cosine similarity'], possible_matches['id']))

    # Sort the pairs by cosine similarity in descending order
    sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

    # Unzip the sorted pairs into separate lists
    sorted_books, sorted_similarities, sorted_ids = zip(*sorted_pairs)

    # Rebuild the dictionary with sorted books and similarities
    sorted_possible_matches = {
        'book': list(sorted_books),
        'cosine similarity': list(sorted_similarities),
        'id': list(sorted_ids)
    }
    
    # Return the sorted dictionary of similar books
    return sorted_possible_matches

# Function to search for a book id based on its name
def search_book_id(Book_Name):
    # Fetch the book id from the 'data' DataFrame based on the book's title
    p = data.loc[data['title'] == Book_Name]['id'].values[0]

    return p

# Main loop to allow user to input a book name and find similar books
while True:
    try:
        print('\n')  # Print a new line for formatting
        # Prompt the user for a book name
        Book_Name = input("Give The Name Of a Book: ")
        # Find the corresponding book id for the input book name
        Book_Id = search_book_id(Book_Name)
        # Fetch the similar books' ids and details
        more_similar_books_ids = more_similar_books(Book_Id)['id']
        print('\n')

        # Print the top 5 most similar books along with their Amazon links
        for x in range(5):
            print("Book:", data.loc[data['id'] == (more_similar_books_ids[x])]['title'].values[0])
            print("Amazon Link: ", data.loc[data['id'] == (more_similar_books_ids[x])]['amazon link'].values[0])
            print('\n')
    except:
        # Handle cases where the book is not found or there aren't enough recommendations
        print('\n')
        print("Try Another Book (Not Available In The Dataset/Not Enough Recommendations)")
    
