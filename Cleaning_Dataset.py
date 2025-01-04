import pandas as pd 

# Load dataset
df_dataset = pd.read_csv('PATH_TO_DATASET') #https://www.kaggle.com/datasets/austinreese/goodreads-books

# Select relevant columns
df_dataset = df_dataset[['id', 'title', 'original_title', 'rating_count','description','genre_and_votes','amazon_redirect_link']]

# Drop rows with missing values
df_dataset.dropna(inplace=True)

# Remove numbers from genre_and_votes
df_dataset['genre_and_votes'] = df_dataset['genre_and_votes'].replace(r'\d+', '', regex=True).str.rsplit(",").apply(lambda x: x[0])

# Sort by rating_count in descending order
df_dataset.sort_values(by='rating_count', ascending=False, inplace=True)

# Remove duplicates based on original_title
df_dataset.drop_duplicates(subset=['original_title'], inplace=True)

# Keep top 1,000 rows
df_dataset = df_dataset.head(1000) 

# Drop unnecessary columns
df_dataset.drop(columns=['rating_count','original_title'], inplace=True)

# Set 'id' as the index
df_dataset.set_index('id', inplace=True)

# Rename columns for clarity
df_dataset.rename(columns={ 'genre_and_votes': 'genre', 'amazon_redirect_link': 'amazon link'}, inplace=True)

#Save as CSV
df_dataset.to_csv("Books Data.csv")
