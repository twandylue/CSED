import joblib  # saving the model
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import (
    MultinomialNB,
)
from sklearn.pipeline import Pipeline


def train_by_naive_bayes(file_name: str = "./data/spam.csv"):
    """
    Train the model using the Naive Bayes algorithm
    :param file_name: the file name of the dataset
    """
    data: pd.DataFrame = pd.read_csv(file_name)
    data["Spam"] = data["Category"].apply(lambda x: 1 if x == "spam" else 0)

    """
    NOTE:
    Splitting the data into training and testing data. Here 75% of the data is used for training and 25% for testing
    """
    X_train, X_test, y_train, y_test = train_test_split(
        data.Message, data.Spam, test_size=0.25
    )

    """
    NOTE:
    1. This can be replaced and tested with other classifiers
    2. Naive Bayes Have three Classifier(Bernouli,Multinominal,Gaussian).
    Here I use Multinominal Bayes because here data in a discrete form discrete data(e.g movie ratings ranging 1 to 5 as each rating will have certain frequency to represent)
    """
    clf = Pipeline([("vectorizer", CountVectorizer()), ("nb", MultinomialNB())])
    print("Starting to train the model...")
    result: MultinomialNB = clf.fit(X_train, y_train)
    print("Model trained")
    print(f"Accuracy: {result.score(X_test, y_test):.4f}")

    # Saving the model
    print("Saving the model...")
    try:
        joblib.dump(clf, "./data/spam_model.pkl")
        print("Model saved")
    except Exception as e:
        print(f"Error: {e}")
