import streamlit as st
import pickle
import pandas as pd
import random
from src.remove_ import remove

# Set page config
st.set_page_config(page_title="Mobile Recommender System", page_icon="📱", layout="wide", initial_sidebar_state="expanded")

# Load data with error handling
try:
    df = pickle.load(file=open(file=r'src/model/dataframe.pkl', mode='rb'))
    similarity = pickle.load(file=open(file=r'src/model/similarity.pkl', mode='rb'))
except Exception as e:
    st.error(f"Error loading data files: {e}")
    st.stop()

remove()

# Exchange rate: INR to LKR
INR_TO_LKR = 3.6  # Update with current rate

def convert_to_lkr(price):
    """Convert price from INR to LKR, no decimals."""
    try:
        price_str = str(price).replace('₹', '').replace(',', '').strip()
        price_numeric = float(price_str)
        return int(price_numeric * INR_TO_LKR)
    except (ValueError, TypeError) as e:
        st.warning(f"Price conversion error: {e}")
        return price

def recommend_different_variety(mobile, filters):
    try:
        mobile_index = df[df['name'] == mobile].index[0]
        similarity_array = similarity[mobile_index]
        different_variety = random.sample(list(enumerate(similarity_array)), k=min(10, len(similarity_array)))
        results = [(df['name'].iloc[i[0]], fetch_IMG(i[0]), df['ratings'].iloc[i[0]], convert_to_lkr(df['price'].iloc[i[0]])) for i in different_variety]
        return apply_filters(results, filters)
    except Exception as e:
        st.error(f"Error in recommend_different_variety: {e}")
        return []

def recommend(mobile, filters):
    try:
        mobile_index = df[df['name'] == mobile].index[0]
        similarity_array = similarity[mobile_index]
        similar_10_mobiles = sorted(list(enumerate(similarity_array)), reverse=True, key=lambda x: x[1])[1:11]
        results = [(df['name'].iloc[i[0]], fetch_IMG(i[0]), df['ratings'].iloc[i[0]], convert_to_lkr(df['price'].iloc[i[0]])) for i in similar_10_mobiles]
        return apply_filters(results, filters)
    except Exception as e:
        st.error(f"Error in recommend: {e}")
        return []

def fetch_IMG(mobile_index):
    try:
        return df['imgURL'].iloc[mobile_index]
    except Exception as e:
        st.warning(f"Image fetch error: {e}")
        return "https://via.placeholder.com/120"  # Placeholder image

def apply_filters(results, filters):
    try:
        filtered = results
        price_range, min_rating = filters  # Only price and rating filters
        filtered = [item for item in filtered if price_range[0] <= item[3] <= price_range[1] and item[2] >= min_rating]
        return filtered
    except Exception as e:
        st.error(f"Error in apply_filters: {e}")
        return []

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&family=Roboto:wght@400&display=swap');
    .main {background-color: #e6f0fa;}
    .stButton>button {
        background-color: #007bff;
        color: #ffffff !important;
        border-radius: 10px;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: 600;
        border: 2px solid #0056b3;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        color: #ffffff !important;
        border-color: #003d82;
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        text-align: center;
        transition: transform 0.2s;
        min-height: 300px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card:hover {
        transform: scale(1.05);
    }
    .card img {
        max-width: 120px;
        margin-bottom: 10px;
        border-radius: 8px;
    }
    .card p {
        margin: 5px 0;
        font-size: 16px;
        color: #333;
        word-wrap: break-word;
    }
    .card b {
        font-size: 18px;
        color: #2c3e50;
    }
    .header-container {
        background: linear-gradient(135deg, #007bff 0%, #00c6ff 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
        animation: fadeIn 1.5s ease-in-out;
    }
    .title {
        font-family: 'Poppins', sans-serif;
        font-size: 48px;
        font-weight: 700;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        margin: 0;
    }
    .subtitle {
        font-family: 'Roboto', sans-serif;
        font-size: 24px;
        color: #f0f8ff;
        margin-top: 10px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .footer {
        text-align: center;
        padding: 20px;
        color: #7f8c8d;
        font-size: 16px;
    }
    @keyframes fadeIn {
        0% {opacity: 0; transform: translateY(-20px);}
        100% {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# Enhanced Header
st.markdown("""
    <div class="header-container">
        <div class="title">Mobile Recommender System 📱</div>
        <div class="subtitle">Discover Your Perfect Mobile with Ease At SmartX</div>
    </div>
""", unsafe_allow_html=True)

# Sidebar with filters (only price and rating)
with st.sidebar:
    st.header("Filter Options")
    price_range = st.slider("Price Range (Rs)", min_value=0, max_value=100000, value=(0, 100000), step=1000)
    min_rating = st.slider("Minimum Rating", min_value=0.0, max_value=5.0, value=0.0, step=0.1)

# Main content
mobiles = df['name'].values
selected_mobile = st.selectbox(label="Select Mobile Name", options=mobiles, help="Pick a mobile to see tailored recommendations")

if st.button("Recommend"):
    with st.spinner("Loading recommendations..."):
        filters = (price_range, min_rating)  # Reduced filter tuple
        recommended = recommend(selected_mobile, filters)
        variety = recommend_different_variety(selected_mobile, filters)

        # Recommended Mobiles Section
        st.markdown("### Top Recommendations")
        if recommended:
            cols = st.columns(5)
            for i, (name, img, rating, price) in enumerate(recommended[:5]):
                with cols[i]:
                    st.markdown(f"""
                        <div class="card">
                            <img src="{img}" alt="{name}">
                            <p><b>{name}</b></p>
                            <p>Rating: {rating}</p>
                            <p>Price: Rs {price:,}</p>
                        </div>
                    """, unsafe_allow_html=True)

            if len(recommended) > 5:
                cols = st.columns(5)
                for i, (name, img, rating, price) in enumerate(recommended[5:10]):
                    with cols[i]:
                        st.markdown(f"""
                            <div class="card">
                                <img src="{img}" alt="{name}">
                                <p><b>{name}</b></p>
                                <p>Rating: {rating}</p>
                                <p>Price: Rs {price:,}</p>
                            </div>
                        """, unsafe_allow_html=True)
        else:
            st.warning("No recommendations match your filters.")

        # Variety Section
        st.markdown("---")
        st.markdown("### Explore More Options")
        if variety:
            cols = st.columns(5)
            for i, (name, img, rating, price) in enumerate(variety[:5]):
                with cols[i]:
                    st.markdown(f"""
                        <div class="card">
                            <img src="{img}" alt="{name}">
                            <p><b>{name}</b></p>
                            <p>Rating: {rating}</p>
                            <p>Price: Rs {price:,}</p>
                        </div>
                    """, unsafe_allow_html=True)

            if len(variety) > 5:
                cols = st.columns(5)
                for i, (name, img, rating, price) in enumerate(variety[5:10]):
                    with cols[i]:
                        st.markdown(f"""
                            <div class="card">
                                <img src="{img}" alt="{name}">
                                <p><b>{name}</b></p>
                                <p>Rating: {rating}</p>
                                <p>Price: Rs {price:,}</p>
                            </div>
                        """, unsafe_allow_html=True)
        else:
            st.warning("No variety options match your filters.")

# Footer
st.markdown("---")
st.markdown('<div class="footer">Thank You for Visiting 🙂 | Made by 👨🏻‍💻 Sudeepa Wanigarathna</div>', unsafe_allow_html=True)
