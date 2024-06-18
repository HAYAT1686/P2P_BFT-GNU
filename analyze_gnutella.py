import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def analyze_gnutella(df):
    
    G = nx.from_pandas_edgelist(df, source='Source', target='Target')
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")

    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    plt.loglog(degree_sequence, marker='o', linestyle='None')
    plt.title('Gnutella Network Degree Distribution')
    plt.xlabel('Rank')
    plt.ylabel('Degree')
    plt.show()

if __name__ == "__main__":
    gnutella_data = pd.read_csv("C:/Users/janvi/OneDrive/Desktop/P2P_BYZANTINE_PROB/Data/Gnutella/p2p-Gnutella08.txt.gz", sep='\t', header=None, names=['Source', 'Target'])
    analyze_gnutella(gnutella_data)
