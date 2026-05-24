import joblib
import pandas as pd


model = joblib.load(
    "model/wine_binary_model.pkl"
)

FEATURES = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol"
]

def predict_wine(data: dict):

    df = pd.DataFrame([data])

    df = df[FEATURES]

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0]

    label = (
        "High Quality"
        if prediction == 1
        else "Low Quality"
    )

    confidence = float(
    round(max(probability) * 100, 2)
)

    return {
    "prediction": label,
    "confidence": confidence,
    "probability_low_quality": round(
        float(probability[0]) * 100,
        2
    ),
    "probability_high_quality": round(
        float(probability[1]) * 100,
        2
    )
}
    

