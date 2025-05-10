# Copyright (c) 2025 Kemar Christie
# Authors: Kemar Christie

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Define path to save model in "code" subdirectory
model_path = os.path.join("code", "local_ml_model.pkl")

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save model
with open(model_path, "wb") as f:
    pickle.dump(model, f)


# Print statement to let you know that the model was saved sucessfully
print(f"✅ Model saved to {os.path.abspath(model_path)}")