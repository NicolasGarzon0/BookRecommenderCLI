# BookRecommenderCLI

**BookRecommenderCLI** is a command-line application that recommends books based on user input. By entering the name of a book, the user receives 5 book recommendations, each with an Amazon link. The app generates these recommendations by analyzing the book's description and genre, leveraging feature vectors and cosine similarity to calculate similarity. 

## App in Action
![App Demo](App%20Demo.GIF)  <!-- Ensure the image path is correct -->

## Running The App

1. Clone the repository:
    ```bash
    git clone https://github.com/NicolasGarzon0/BookRecommenderCLI.git
    ```

2. Navigate into the project directory:
    ```bash
    cd BookRecommenderCLI
    ```

3. The repository already includes the pre-processed files inside the `CSV Files` folder:
    - `Books Data.csv`
    - `Recommendation Vectors.csv`

    To minimize file size, these files include data for only the 1,000 most-reviewed books in the dataset. However, this can be modified by adjusting the Jupyter Notebook (`Data_Cleaning_and_Recommendation_Vectors.ipynb`) to include more books of the original dataset.

    Open the `app.py` file and update it with your local paths to these files. These paths will be used by the application to load the necessary data.

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:
    ```bash
    python app.py
    ```

6. When prompted, enter the name of a book to receive 5 recommended books along with their Amazon links.

## Dataset

The app utilizes a Kaggle dataset containing 50,000 Goodreads books, which includes book titles, authors, genres, descriptions, ratings, and more. The dataset can be found and downloaded [here](https://www.kaggle.com/datasets/austinreese/goodreads-books).

### Pre-Processing

The repository includes a Jupyter Notebook (`Data_Cleaning_and_Recommendation_Vectors.ipynb`) that documents the process of creating the `Books Data.csv` and `Recommendation Vectors.csv` files. This notebook demonstrates how the Kaggle dataset was cleaned and transformed to create the feature vectors used in the recommendation engine. You can review the notebook for details on the preprocessing steps if needed.

## Technologies Used

- Python
- Pandas
- Numpy
- Scikit-learn
