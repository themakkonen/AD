import pandas as pd
import numpy as np

# Create a synthetic dataset
np.random.seed(42)
num_samples = 1000

data = {
    'phone_number': [f'123456789{i % 10}' for i in range(num_samples)],
    'amount': np.random.uniform(1, 1000, num_samples),
    'transaction_type': np.random.choice(['payment', 'refund'], num_samples),
    'isFraud': np.random.choice([0, 1], num_samples, p=[0.9, 0.1])  # 10% fraud
}

df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv('transact_dataset.csv', index=False)
print("Synthetic dataset created and saved as 'transact_dataset.csv'.")