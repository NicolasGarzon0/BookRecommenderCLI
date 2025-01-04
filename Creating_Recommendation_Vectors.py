import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer

# Load Dataset
data = pd.read_csv('PATH_TO_Books Data.csv')

#Normalized Genres
Normalized_Genres = pd.get_dummies(data['genre'], dtype='int')

# Normalized Descriptions using TF-IDF
data['description'] = data['description'].str.lower()
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
tfidf_matrix = vectorizer.fit_transform(data['description']).toarray()
tfidf_df = pd.DataFrame(tfidf_matrix, columns=vectorizer.get_feature_names_out())

#Combined Dataframe
Revised_Dataframe = pd.DataFrame()
Revised_Dataframe = pd.concat([Normalized_Genres,tfidf_df,data['id']], axis=1)
Revised_Dataframe.set_index("id", inplace=True)

#Save as CSV
Revised_Dataframe.to_csv("Recommendation Vectors.csv", index=True)
