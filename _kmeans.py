from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1], [2], [3], [10], [11], [12]])

model = KMeans(n_clusters=2, random_state=42)
model.fit(X)

print("Cluster Labels:", model.labels_)
