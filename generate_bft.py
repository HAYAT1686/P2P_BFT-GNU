import pandas as pd
import numpy as np
import os

def generate_bft_sample_data(num_entries=1000, output_path="C:/Users/janvi/OneDrive/Desktop/P2P_BYZANTINE_PROB/Data/BFT/bft_sample_data.csv"):
    """
    Parameters:
    - num_entries (int): Number of data entries to generate.
    - output_path (str): Path to save the generated sample data.
    """
    np.random.seed(42)  # For reproducibility

    data = {
        'node_id': np.arange(num_entries),
        'is_byzantine': np.random.choice([0, 1], size=num_entries, p=[0.95, 0.05]),  # 5% Byzantine nodes
        'request_id': np.random.randint(1000, 10000, size=num_entries),
        'response_time': np.random.normal(loc=200, scale=50, size=num_entries),  # Response time in ms
        'response_correct': np.random.choice([0, 1], size=num_entries, p=[0.1, 0.9])  # 90% correct responses
    }

    # Introduce faults in Byzantine nodes
    byzantine_indices = data['is_byzantine'] == 1
    data['response_correct'][byzantine_indices] = np.random.choice([0, 1], size=sum(byzantine_indices), p=[0.7, 0.3])

    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"BFT sample data generated with {df.shape[0]} rows and saved to {output_path}")

if __name__ == "__main__":
    generate_bft_sample_data()
