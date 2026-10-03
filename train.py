from sklearn.linear_model import LinearRegression
import pickle

# Sample training data
X = [
    [2, 60, 50],
    [3, 65, 55],
    [4, 70, 60],
    [5, 75, 65],
    [6, 80, 70],
    [7, 85, 75],
    [8, 90, 80],
    [9, 95, 85]
]

y = [
    50,
    55,
    60,
    65,
    70,
    75,
    80,
    85
]

model = LinearRegression()
model.fit(X, y)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")