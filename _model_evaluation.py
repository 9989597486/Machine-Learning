from sklearn.metrics import accuracy_score

actual = [1, 0, 1, 1]
predicted = [1, 0, 0, 1]

accuracy = accuracy_score(actual, predicted)

print("Accuracy:", accuracy)
