import os
import pandas as pd

for file in os.listdir():
    if file.endswith("json"):
        reviews_data = pd.read_json("yelp_academic_dataset_review_41.json")
        print(reviews_data.head())
        break
