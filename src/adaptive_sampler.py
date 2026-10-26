
import time


SAMPLING_RATES = {
    "active": 30,
    "idle": 4,
    "deep_idle": 1,
}


class AdaptiveSampler:
    """Decide when a frame should be stored for each motion state."""

    def __init__(self):
        self.last_saved_time = None
        self.last_state = None

    def should_save(self, state, now=None):
        if state not in SAMPLING_RATES:
            raise ValueError(f"Unknown motion state: {state}")

        if now is None:
            now = time.monotonic()

        state_changed = state != self.last_state
        fps = SAMPLING_RATES[state]
        interval = 1.0 / fps

        if (
            self.last_saved_time is None
            or state_changed
            or now - self.last_saved_time >= interval
        ):
            self.last_saved_time = now
            self.last_state = state
            return True

        return False
