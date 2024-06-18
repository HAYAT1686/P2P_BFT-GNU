import pandas as pd

def load_gnutella_data(file_path):
    return pd.read_csv(file_path, sep='\t', header=None, names=['Source', 'Target'])

if __name__ == "__main__":
    gnutella_data = load_gnutella_data("C:/Users/janvi/OneDrive/Desktop/P2P_BYZANTINE_PROB/Data/Gnutella/p2p-Gnutella08.txt.gz")
    print(f"Gnutella data loaded with {gnutella_data.shape[0]} rows and {gnutella_data.shape[1]} columns.")
