import pandas as pd
import matplotlib.pyplot as plt

def analyze_bft(df):

    print(df.describe())

    # Plot histogram of response times
    plt.hist(df['response_time'], bins=30, alpha=0.7, label='Response Time')
    plt.title('BFT Response Time Distribution')
    plt.xlabel('Response Time (ms)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

    # Plot histogram of correct responses
    plt.hist(df['response_correct'], bins=2, alpha=0.7, label='Correct Responses')
    plt.title('BFT Correct Responses Distribution')
    plt.xlabel('Correct Response (0 = Incorrect, 1 = Correct)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

    # Plot proportion of Byzantine nodes
    byzantine_proportion = df['is_byzantine'].mean()
    plt.bar(['Non-Byzantine', 'Byzantine'], [1 - byzantine_proportion, byzantine_proportion], color=['blue', 'red'])
    plt.title('Proportion of Byzantine Nodes')
    plt.ylabel('Proportion')
    plt.show()

if __name__ == "__main__":
    bft_data = pd.read_csv("C:/Users/janvi/OneDrive/Desktop/P2P_BYZANTINE_PROB/Data/BFT/bft_sample_data.csv")
    analyze_bft(bft_data)
