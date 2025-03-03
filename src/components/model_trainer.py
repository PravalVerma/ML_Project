from sklearn.preprocessing import StandardScaler
import numpy as np

data = np.array([[10, 200], [20, 300], [30, 400]])  # Sample data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print(scaled_data)
