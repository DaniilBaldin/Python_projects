from timeit import default_timer
from time import time

from flask.wrappers import Request


class Timer:
    def __init__(self, file_name, request: Request):
        self.file_name = file_name
        self.request = request
        self.timer = default_timer
        self.time = time

    def __enter__(self):
        self.start = self.timer()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = self.timer()
        self.elapsed_secs = end - self.start
        self.elapsed = float('{:.3f}'.format(self.elapsed_secs * 1000))
        error = exc_val if exc_type is not None else ""
        path = self.request.path
        with open(self.file_name, "a") as file:
            file.write(
                f"Task finished in {self.elapsed} milliseconds {error}. {path}\n"
            )
