import numpy as np

def run():
    print("✅ Loading data from /tmp/data.npy...")
    data = np.load("/tmp/data.npy")
    print("Data loaded:", data)
    print("Mean value:", np.mean(data))

if __name__ == "__main__":
    run()
