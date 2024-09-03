import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate some sample data (normal data and a few anomalies)
data = np.random.normal(50, 5, 100)  # 100 data points with mean=50, std=5
anomalies = np.array([70, 75, 80])  # Add some anomalies
data = np.concatenate([data, anomalies])

# Step 2: Calculate the Z-scores for each data point
mean = np.mean(data)
std_dev = np.std(data)
z_scores = [(x - mean) / std_dev for x in data]

# Step 3: Set a threshold to detect anomalies (e.g., Z-score > 3 or < -3)
threshold = 3
anomaly_indices = [i for i, z in enumerate(z_scores) if abs(z) > threshold]

# Step 4: Visualize the results
plt.figure(figsize=(9, 6))
plt.plot(data, label='Data')
plt.scatter(anomaly_indices, data[anomaly_indices], color='red', label='Anomalies')
plt.title('Anomaly Detection using Z-Score')
plt.xlabel('Data Point Index')
plt.ylabel('Value')
plt.legend()
plt.show()
