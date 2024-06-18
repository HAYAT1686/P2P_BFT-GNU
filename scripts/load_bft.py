import pandas as pd

def load_bft_data(file_path):

    return pd.read_csv(file_path)

if __name__ == "__main__":
    bft_data = load_bft_data("C:/Users/janvi/OneDrive/Desktop/P2P_BYZANTINE_PROB/Data/BFT/bft_sample_data.csv")
    print(f"BFT data loaded with {bft_data.shape[0]} rows and {bft_data.shape[1]} columns.")
