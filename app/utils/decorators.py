import time                     # Import time module to measure runtime
from functools import wraps     # Import wraps to keep function metadata

def timed(fn):
    # This decorator will measure how long a function takes to run
    # and add the elapsed time into the dictionary result.
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.time()        # Record start time
        out = fn(*args, **kwargs)   # Run the actual function
        if isinstance(out, dict):  # Only add timing if the result is a dict
            out["_elapsed_sec"] = round(time.time() - t0, 3)
        return out              # Return the result (with time added)
    return wrapper              # Return the wrapper function

def validate_input(expected_types):
    # This decorator checks that the input to a function
    # is of the correct type(s).
    def deco(fn):
        @wraps(fn)
        def wrapper(self, data, *args, **kwargs):
            if not isinstance(data, expected_types):  # Check input type
                raise TypeError(f"Expected {expected_types}, got {type(data)}")
            return fn(self, data, *args, **kwargs)    # Run the function if type is correct
        return wrapper
    return deco
