import numpy as np


def generate(p1):
    seed = None
    rng = np.random.default_rng(seed)
    return rng.choice([0, 1], p=[1 - p1, p1], size=10000)


def count(seq):
    seq_str = ''.join(map(str, seq))  # Convert sequence to a string
    cnt = 0

    # Sliding window search and to count not only distinct occurrences
    idx = 0
    while idx <= len(seq_str) - 5:
        if seq_str[idx:idx + 5] == "11111":
            cnt += 1
            idx += 1
        else:
            idx += 1
    return cnt

def main(p1):
    seq = generate(p1)
    return count(seq)


p1 = 2 / 3
observed_count = main(p1)
expected_count = 10000 * (p1) ** 5  # ≈ 1316.9

# Print results
print(f"Observed count: {observed_count}")
print(f"Expected count: {expected_count:.1f}")
print(f"Difference: {abs(observed_count - expected_count):.1f}")
