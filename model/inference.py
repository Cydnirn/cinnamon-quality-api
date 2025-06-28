import pickle
import pandas as pd

cinnamon_model = pickle.load(open('./model/cinnamon.pkl', 'rb'))

def create_custom_sample(moisture, ash, oil, acid, chromium, coumarin):
    custom_sample_hardcoded = pd.DataFrame({
        'Moisture (%)': [moisture],
        'Ash (%)': [ash],
        'Volatile_Oil (%)': [oil],
        'Acid_Insoluble_Ash (%)': [acid],
        'Chromium (mg/kg)': [chromium],
        'Coumarin (mg/kg)': [coumarin],
    })
    return custom_sample_hardcoded

def predict_cinnamon_quality(sample):
    prediction = cinnamon_model.predict(sample)
    probability = cinnamon_model.predict_proba(sample)
    confidence = probability.max() * 100
    return prediction[0], confidence
