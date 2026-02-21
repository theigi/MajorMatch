import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import os

def train():
    # Adjusted path to find data relative to the script location
    data_path = os.path.join(os.path.dirname(__file__), '../data/student_data.csv')
    df = pd.read_csv(data_path)
    
    le_i, le_m = LabelEncoder(), LabelEncoder()
    df['InterestEncoded'] = le_i.fit_transform(df['Interest'])
    df['MajorEncoded'] = le_m.fit_transform(df['RecommendedMajor'])
    
    X = df[['MathScore', 'PhysicsScore', 'ChemistryScore', 'EnglishScore', 'InterestEncoded']]
    y = df['MajorEncoded']
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    # Save to the new ml_models directory
    model_dir = os.path.join(os.path.dirname(__file__), '../ml_models')
    os.makedirs(model_dir, exist_ok=True)
    
    with open(os.path.join(model_dir, 'model.pkl'), 'wb') as f: pickle.dump(model, f)
    with open(os.path.join(model_dir, 'le_interest.pkl'), 'wb') as f: pickle.dump(le_i, f)
    with open(os.path.join(model_dir, 'le_major.pkl'), 'wb') as f: pickle.dump(le_m, f)
    print(f"✅ Models saved in {model_dir}")

if __name__ == "__main__":
    train()