# Two-Stage Recommender System

## Table of Contents
- [Overview](#overview)
- [Current System](#current-system)
- [Modelling](#modelling)
- [Future Considerations](#future-considerations)
- [References](#references)

## Overview
This repository contains a prototype content recommendation model developed for an online news platform. The model is designed to provide personalised article recommendations to users based on their past interactions and article metadata. This prototype, when completed, could replace the current model that recommends articles based on click through rate.

## Current System
### Data Ingestion
- Pros:
  - Real-time data collection: immediate collection of session timestamps, article clicks, and system/device versions.

- Cons:
  - Limited features, limited personalisation: despite immediate collection of data, it captures a small number of features.
  - Potential data quality issues: ad-blockers are common among users concerned about privacy and security. These extensions often block JavaScript by default to prevent tracking and enhance security. Therefore, the use of JavaScript for full data ingestion could compromise model training and recommendation due to increased bias from fewer users.


### Modelling
- Pros:
  - Simplicity: easy to implement and maintain.
- Cons:
  - Lack of personalisation: 'one size fits all' approach not tailored to individual user preferences. It might also neglect niche content.
  - Static recommendations: weekly updates may not capture rapid user preference changes. Topics such as geopolitics and sports require more frequent updates.

### Deployment
- Pros:
  - Scalability: Amazon SageMaker enables scalable model training and deployment.

- Cons:
  - Fixed schedule: it might not adapt quickly to content trend changes.
  - Potential downtime: recommendations may be unavailable during retraining and deployment.

### Monitoring
- Pros:
  - Key metrics: `CTR` and `average time spent` provide a foundation for evaluating engagement.

- Cons:
  - Limited metrics: current set of metrics overlooks teh distinction between model (e.g. recall, drift) metrics and business/engagement metrics (*e.g.* user retention, satisfaction, and churn).

**Summary**
The current system provides a basic framework but lacks further personalisation, interaction data, and monitoring using different types of metrics.


## Modelling
The prototype is inspired by Covington *et al.* (2016) paper on YouTube recommendations. Researchers used a two-stage approach, efficiently separating candidate generation from ranking outperforming previous matrix factorization approaches by Weston *et al*. (2011). The two-stage approach demonstrates high scalability and effectiveness in large-scale settings.

### Step 1: Similar Article Retrieval
The first stage uses collaborative filtering to generate candidate recommendations based on user-item interactions. More specifically, it leverages the article embeddings and nearest neighbor search to identify similar articles.

### Step 2: Ranking and Personalisation
In the second stage, the model ranks these candidates using features such as user online behaviour, article metadata, clicks, and content embeddings. XGBoost is utilised because of its strong capability to handle complex relationships and provide accurate rankings.



## Future Recommendation
- low-rank quantization
- deep learning
- vs predicting click-through rate directly

data ingestion
it does not track detailed engagement metrics like scroll depth, dwell time, likes, comments, and shares. These could be useful to improve user-item filtering. In case of asubscription model, it would be valuable to track daily active users (DAU) and monthly active users (MAU) A healthy ratio of DAU/MAU (*aka* stickiness) suggests that a significant portion of monthly users are returning daily, indicating strong retention and user satisfaction

Rolling updates and A/B testing minimise downtime.

### References
Covington, P., Adams, J., & Sargin, E. (2016). Deep Neural Networks for YouTube Recommendations. *Proceedings of the 10th ACM Conference on Recommender Systems (RecSys '16)*, 191-198.

Weston, J., Bengio, S., & Usunier, N. (2011). Wsabie: Scaling up to large vocabulary image annotation. In Proceedings of the 22nd International Joint Conference on Artificial Intelligence (IJCAI), 1466-1471.
