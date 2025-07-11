import sys
import numpy as np

def run():
    if len(sys.argv) > 1:
        try:
            size = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid argument: Please provide an integer.")
            return
    else:
        size = 2  # default size

    matrix = np.random.rand(size, size)
    print(f"✅ Generated {size}x{size} matrix:")
    print(matrix)

if __name__ == "__main__":
    run()
