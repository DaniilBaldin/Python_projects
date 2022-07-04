from timeit import default_timer


class Timer:
    def __init__(self, name):
        self.file = open(name, 'a')
        self.timer = default_timer

    def __enter__(self):
        self.start = self.timer()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = self.timer()
        self.elapsed_secs = end - self.start
        self.elapsed = float('{:.3f}'.format(self.elapsed_secs * 1000))
        result_text = "Successful" if not exc_type else exc_val
        self.file.write(f"Function finished in {self.elapsed} milliseconds. Result: {result_text}\n")
        self.file.close()
        return True


def numbers(start, end):
    if type(start) is not int:
        raise TypeError("Error: start and end must be int")
    elif type(end) is not int:
        raise TypeError("Error: Start and end must be int")
    elif start >= end:
        raise ValueError("Error: Start must be less than end")

    x = start
    while x < end:
        yield x
        x += 1


with Timer("file.txt"):
    for i in numbers(10, 20):
        print(i)


with Timer("file.txt"):
    for i in numbers(10, 10):
        print(i)


with Timer("file.txt"):
    for i in numbers("asd", "asd"):
        print(i)
