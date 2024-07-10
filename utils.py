import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(data_path):
  """
  Loads data from a CSV file.

  Args:
      data_path (str): Path to the CSV file.

  Returns:
      pd.DataFrame: The loaded dataframe.
  """
  return pd.read_csv(data_path)

def preprocess_data(data):
  """
  Prepares data for model training/prediction.

  Args:
      data (pd.DataFrame): The dataframe to preprocess.

  Returns:
      pd.DataFrame: The preprocessed dataframe with scaled features.
  """
  # separate features and target variable
  columns_to_keep = ['user_id',	'candidate_article_id',	'click_article_id',
                     'session_size', 'click_environment', 'click_deviceGroup',
                     'click_os', 'click_country', 'click_referrer_type', 'time_diff']

  features = data[columns_to_keep]

  # Apply MinMax scaling to features
  scaler = MinMaxScaler()
  scaled_features = scaler.fit_transform(features)

  return pd.DataFrame(scaled_features, columns=features.columns), target

def predict_top_article(data, model):
  """
  Predicts the top-ranked article (candidate article) based on NDCG score.

  Args:
      data (pd.DataFrame): The data to predict on (features).
      model: The trained model for prediction.

  Returns:
      int: The predicted candidate_article_id with the highest NDCG score.
  """
  # Predict NDCG scores for all candidate articles
  predictions = model.predict(data)

  # Assuming the model directly predicts NDCG scores
  # (adapt if model outputs probabilities or rankings)
  # Get the index of the article with the highest predicted NDCG score
  top_article_idx = predictions.argmax()

  # Extract the corresponding candidate_article_id from the data
  candidate_article_id = data.iloc[top_article_idx]['candidate_article_id']

  return candidate_article_id

# Example usage (assuming your CSV is named 'data.csv')
data = load_data('data.csv')
features, target = preprocess_data(data.copy())  # Avoid modifying original data
predicted_article_id = predict_top_article(features, model)

print(f"Predicted top article (candidate_article_id): {predicted_article_id}")
