
from adaptive_sampler import AdaptiveSampler


def main():
    sampler = AdaptiveSampler()

    print("Testing idle sampling at 4 FPS")
    for timestamp in [0.0, 0.1, 0.2, 0.25, 0.3, 0.5, 0.75]:
        print(
            f"t={timestamp:.2f}s -> "
            f"{'SAVE' if sampler.should_save('idle', timestamp) else 'SKIP'}"
        )


if __name__ == "__main__":
    main()
