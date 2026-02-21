import pickle
import os

class MajorPredictor:
    def __init__(self, model_dir="ml_models/"):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../", model_dir))
        with open(os.path.join(base_path, 'model.pkl'), 'rb') as f: self.model = pickle.load(f)
        with open(os.path.join(base_path, 'le_interest.pkl'), 'rb') as f: self.le_interest = pickle.load(f)
        with open(os.path.join(base_path, 'le_major.pkl'), 'rb') as f: self.le_major = pickle.load(f)

    def predict(self, math, physics, chemistry, english, interest):
        interest_enc = self.le_interest.transform([interest])[0]
        features = [[math, physics, chemistry, english, interest_enc]]
        pred = self.model.predict(features)
        return self.le_major.inverse_transform(pred)[0]

predictor_instance = None
def get_predictor():
    global predictor_instance
    if predictor_instance is None: predictor_instance = MajorPredictor()
    return predictor_instance