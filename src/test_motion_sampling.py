
from adaptive_sampler import AdaptiveSampler


def main():
    sampler = AdaptiveSampler()

    # Simulated motion states and timestamps.
    frames = [
        (0.00, "idle"),
        (0.10, "idle"),
        (0.20, "active"),
        (0.21, "active"),
        (0.24, "active"),
        (0.50, "idle"),
        (0.60, "idle"),
        (1.00, "deep_idle"),
    ]

    print("Time | Motion state | Save frame?")
    print("-" * 36)

    saved_count = 0

    for timestamp, state in frames:
        save_frame = sampler.should_save(state, timestamp)

        if save_frame:
            saved_count += 1

        print(
            f"{timestamp:4.2f} | "
            f"{state:12} | "
            f"{'YES' if save_frame else 'NO'}"
        )

    print(f"\nFrames selected: {saved_count} of {len(frames)}")


if __name__ == "__main__":
    main()
