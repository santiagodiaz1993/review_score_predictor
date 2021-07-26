from fsplit.filesplit import Filesplit


fs = Filesplit()

fs.split(
    file="yelp_academic_dataset_review.json",
    split_size=1000000000 / 10,
    output_dir="review_data",
)
