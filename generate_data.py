import numpy as np

def run():
    print("✅ Generating data...")
    data = np.random.rand(3, 3)
    np.save("/tmp/data.npy", data)
    print("✅ Data saved to /tmp/data.npy")

if __name__ == "__main__":
    run()
