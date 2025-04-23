Mobile Recommender System
A sleek Streamlit web app to recommend mobile phones based on user selection, with filters for price and ratings. Displays recommendations in LKR (Rs) with images, leveraging content-based filtering and cosine similarity for personalized suggestions.
Features

Select a mobile and get top 10 similar phones and 10 varied options.
Filter by price range and minimum rating.
Modern UI with card-based displays, gradient header, and animations.

Installation

Clone the repository:git clone <repository-url>
cd mobile-recommender-system


Install dependencies:pip install streamlit pandas


Ensure src/model/dataframe.pkl and src/model/similarity.pkl are in place.

Usage

Run the app:streamlit run app.py


Open the browser at http://localhost:8501.
Select a mobile, adjust filters, and click "Recommend" to view results.

Algorithms

Content-Based Filtering: Uses features from the corpus column.
Cosine Similarity: Computes similarity between mobiles based on vectorized text data.
Random Sampling: Introduces variety in recommendations.

Data

dataframe.pkl: Contains columns: name, ratings, price, imgURL, corpus.
similarity.pkl: Precomputed similarity matrix for mobiles.

Contributing
Contributions are welcome! Submit a pull request or open an issue for suggestions.
Author
Sudeepa Wanigarathna
