import streamlit as st
from utils import load_model, transform_user_data, recommend_articles
import pandas as pd

# Load model
model_path = "models/xgboost_recommender.model"
model = load_model(model_path)

# Streamlit app layout
st.title("News Feed Recommender System")

# Drag and drop file upload
uploaded_file = st.file_uploader("upload a csv file to get a recommendation")

if uploaded_file is not None:
  # Read uploaded data
  data = pd.read_csv(uploaded_file)

  # Display data summary (optional)
  st.write(data.head())

  # Preprocess data (assuming preprocessing happens on the full data)
  preprocessed_data = transform_user_data(data)

  # Get prediction (replace with your actual prediction logic using the model)
  predictions = recommend_articles(preprocessed_data, model)

  # Display predictions (assuming predictions are a list or dataframe)
  st.write("predicted click probabilities:")
  st.dataframe(predictions)

else:
  st.info("upload a csv file to get a recommendation")
