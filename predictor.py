# emails = [
#     "Sounds great! Are you home now?",
#     "Will u meet ur dream partner soon? Is ur career off 2 a flyng start? 2 find out free, txt HORO followed by ur star sign, e. g. HORO ARIES",
# ]

import joblib  # saving/loading the model


def predict_by_naive_bayes(input: list[str]) -> None:
    """
    Predict the class of the emails
    :param input: list of emails
    """
    clf = joblib.load("./data/spam_model.pkl")
    result: list[int] = clf.predict(input)
    if result[0] == 1:
        print("Result: This email is Spam.")
        print(f"Probability: {clf.predict_proba(input)[:, 1][0]:.4f}")
        return None
    print("Result: This email is not Spam.")
    print(f"Probability: {clf.predict_proba(input)[:, 0][0]:.4f}")
