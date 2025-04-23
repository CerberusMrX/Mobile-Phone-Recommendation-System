📱 Mobile Recommender System

A sleek Streamlit web application that recommends mobile phones based on user preferences using content-based filtering. The app allows users to filter phones by price range and minimum ratings, and presents results in LKR (Rs) with engaging visuals and a modern UI.

✨ Features

    Personalized Recommendations
    Select a mobile to view:

        Top 10 similar phones using cosine similarity

        10 varied phones for broader options

    Filter Options

        Set your price range

        Choose a minimum rating

    Modern UI

        Card-based layout for results

        Gradient header, subtle animations for a polished look

🚀 Installation

    Clone the repository:
    git clone https://github.com/your-username/mobile-recommender-system.git
    cd mobile-recommender-system

    Install dependencies:
    pip install streamlit pandas

    Ensure required files are in place:
    src/model/dataframe.pkl
    src/model/similarity.pkl

▶️ Usage

    Run the app:
    streamlit run app.py

    Open in your browser:
    http://localhost:8501

    Start exploring:

        Select a mobile

        Adjust filters

        Click "Recommend" to view suggestions

🧠 Algorithms

    Content-Based Filtering
    Utilizes the corpus column derived from mobile features

    Cosine Similarity
    Computes similarity scores between mobiles using vectorized data

    Random Sampling
    Adds variety to recommendations by randomly selecting from similar groups

📊 Data

    dataframe.pkl:
    Contains mobile data with fields: name, ratings, price, imgURL, corpus

    similarity.pkl:
    Precomputed cosine similarity matrix based on the corpus

🤝 Contributing

Contributions are welcome!
Feel free to fork the repository, submit a pull request, or open an issue with ideas or bugs

👤 Author

Sudeepa Wanigarathna
