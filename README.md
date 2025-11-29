# 📱 Mobile Recommender System 🛍️

## Smart Mobile Phone Recommendations using Content-Based Filtering

The **Mobile Recommender System** is a sleek, modern **Streamlit web application** that provides personalized mobile phone recommendations based on user preferences. By leveraging **Content-Based Filtering** and **Cosine Similarity**, the app helps users discover devices that closely match their interests, while offering flexible filtering options.

> **Why use this?** Get personalized phone recommendations based on specific features, price, and rating, presented in a modern, easy-to-use interface.

-----

## ✨ Features Overview

The application is built around personalization and a great user experience.

### 🎯 Personalized Recommendations

Based on a mobile phone selected by the user, the system generates two types of recommendations:

  * **Top 10 Similar Phones:** The 10 most similar phones are identified using **Cosine Similarity** on feature-based vectors.

[Image of Content-Based Filtering Process]

  * **10 Varied Options:** A set of 10 phones, selected via **Random Sampling**, is provided to offer a broader range of similar, yet diverse, options.

### 🔍 Filter Options

Users can refine the recommendations instantly using interactive sidebar controls:

  * **Price Range:** Set a minimum and maximum budget (in **LKR/Rs**).
  * **Minimum Rating:** Choose the lowest acceptable rating.

### 🎨 Modern & Responsive UI

  * **Card-Based Results:** Recommendations are displayed in visually appealing, digestible cards.
  * **Polished Look:** Features a gradient header and subtle animations for a premium, professional web application feel.

-----

## 🧠 Core Algorithms

This system relies on robust machine learning techniques for accuracy and variety.

| Algorithm | Role |
| :--- | :--- |
| **Content-Based Filtering** | Generates feature vectors (the 'corpus') for each mobile based on its specifications (e.g., camera, processor, storage). |
| **Cosine Similarity** | Measures the similarity between the feature vectors of the selected phone and all other phones. The higher the score, the more alike the phones are. |
| **Random Sampling** | Used to inject **diversity** by selecting a subset of similar mobiles randomly, preventing users from seeing only near-identical items. |

-----

## 📊 Data & Model Files

The application relies on two precomputed files, which must be present in the `src/model/` directory:

| File Name | Purpose | Data Fields |
| :--- | :--- | :--- |
| `dataframe.pkl` | Primary data source. | `name`, `ratings`, `price` (LKR), `imgURL`, `corpus` (feature string). |
| `similarity.pkl` | Precomputed model. | **Cosine Similarity Matrix** based on the `corpus` column. |

-----

## 🚀 Installation & Setup

Get the application running on your local machine quickly.

### 1\. Clone the Repository

```bash
git clone https://github.com/your-username/mobile-recommender-system.git
cd mobile-recommender-system
```

### 2\. Install Dependencies

You only need `streamlit` and `pandas` to run the application.

```bash
pip install streamlit pandas
```

### 3\. Verify Model Files

Ensure the necessary model files are located in the correct path.

```
src/
└── model/
    ├── dataframe.pkl
    └── similarity.pkl
```

-----

## ▶️ Usage

### Run the App

Execute the main application file using Streamlit:

```bash
streamlit run app.py
```

### Access

Open your web browser and navigate to:

```
http://localhost:8501
```

### Explore Recommendations

1.  **Select a mobile** from the dropdown menu.
2.  **Adjust the filters** (Price Range, Minimum Rating) on the sidebar.
3.  Click the **"Recommend"** button to view your personalized suggestions\!

-----

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\!

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 👤 Author

  * **Sudeepa Wanigarathna**

-----
