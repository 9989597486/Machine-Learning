from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

prediction = model.predict([[4]])
print("Prediction:", prediction[0])
