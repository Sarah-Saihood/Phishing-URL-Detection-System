from flask import Flask, request, render_template
import numpy as np
import pickle
import csv
import requests
import validators
import os
import sys

from feature import FeatureExtraction

app = Flask(__name__)

# Load trained model
try:

    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__))
    )

    model_path = os.path.join(
        base_path,
        "pickle",
        "model.pkl"
    )

    with open(model_path, "rb") as file:
        model = pickle.load(file)

except:
    model = None


def read_sites(filename):

    sites = []

    try:

        base_path = getattr(
            sys,
            '_MEIPASS',
            os.path.dirname(os.path.abspath(__file__))
        )

        file_path = os.path.join(base_path, filename)

        with open(file_path, "r") as file:

            reader = csv.reader(file)

            for row in reader:

                if row:
                    sites.append(row[0].strip())

    except:
        pass

    return sites


phishing_sites = read_sites("phishing_sites.csv")
trusted_sites = read_sites("trusted_sites.csv")


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        url = request.form["url"].strip()

        # Layer 1: URL validation
        if not validators.url(url):

            return render_template(
                "error.html",
                message="Invalid URL structure.",
                url=url
            )

        # Layer 2: HTTPS check
        if not url.startswith("https://"):

            return render_template(
                "error.html",
                message="Warning: URL does not use HTTPS.",
                url=url
            )

        # Layer 3: Check connection
        connection_failed = False

        try:
            requests.get(url, timeout=5)

        except:
            connection_failed = True

        # Layer 4: Blacklist
        if url in phishing_sites:

            if connection_failed:

                return render_template(
                    "phishing.html",
                    url=url,
                    probability=100,
                    status_message="This phishing website appears to be offline or blocked."
                )

            return render_template(
                "phishing.html",
                url=url,
                probability=100,
                status_message="Active phishing website detected."
            )

        # Layer 5: Whitelist
        if url in trusted_sites:

            return render_template(
                "trusted.html",
                url=url,
                probability=100
            )

        # Layer 6: Machine Learning
        if model is None:

            return render_template(
                "error.html",
                message="Model not found. Please train the model first.",
                url=url
            )

        # Extract features
        features = FeatureExtraction(url).getFeaturesList()

        features = np.array(features).reshape(1, 30)

        # Prediction
        prediction = model.predict(features)[0]

        probability = round(
            max(model.predict_proba(features)[0]) * 100,
            2
        )

        # Phishing result
        if prediction == -1:

            return render_template(
                "phishing.html",
                url=url,
                probability=probability,
                status_message="This website is classified as suspicious by the machine learning model."
            )

        # Trusted result
        return render_template(
            "trusted.html",
            url=url,
            probability=probability
        )

    return render_template("index.html")


if __name__ == "__main__":

    app.run(debug=True)