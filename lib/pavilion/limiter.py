import time
import math
from typing import Callable, Tuple, Any


class TimeLimiter:
    """Wraps a call to a function and only calls it if the specified
    cooldown (in seconds) has elapsed since the last call."""

    def __init__(self, func: Callable[[], Any], cooldown: float):
        self.function = func
        self.cooldown = cooldown
        self.last_called = -math.inf

    def __call__(self) -> Tuple[bool, Any]:
        """Calls the function if enough time has passed, and returns
        a tuple containing a boolean indicating whether the function was actually called
        and the return value of the function (or None if it was not called)."""

        current_time = time.time()

        if current_time - self.last_called > self.cooldown:
            res = self.function()
            self.last_called = current_time
            
            return (True, res)

        return (False, None)
