

from adaptive_sampler import AdaptiveSampler


def main():
    sampler = AdaptiveSampler()

    test_frames = [
        (0.00, "active", True),
        (0.02, "active", False),
        (0.04, "active", True),
        (0.30, "idle", True),
        (0.40, "idle", False),
        (0.60, "idle", True),
        (1.00, "deep_idle", True),
        (1.50, "deep_idle", False),
        (2.10, "deep_idle", True),
    ]

    print("Time | State      | Expected | Actual")
    print("-" * 43)

    for timestamp, state, expected in test_frames:
        actual = sampler.should_save(state, timestamp)

        print(
            f"{timestamp:4.2f} | "
            f"{state:10} | "
            f"{'YES' if expected else 'NO':8} | "
            f"{'YES' if actual else 'NO'}"
        )

        assert actual == expected, (
            f"Test failed at time {timestamp:.2f} "
            f"for state '{state}'"
        )

    print("\nAll tests passed!")


if __name__ == "__main__":
    main()
