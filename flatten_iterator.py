# https://techdevguide.withgoogle.com/resources/former-coding-interview-question-flatten-an-iterator-of-iterators

from collections import deque

class IF:
    def __init__(self, iter_list):
        self.queue = deque(iter_list)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.queue) > 0:
            it = self.queue.popleft()
            try:
                e = next(it)
                self.queue.append(it)
                return e
            except StopIteration:
                return next(self)
        else:
            raise StopIteration


it = IF([iter([1,2,3]), iter([4,5,6]), iter([7,8,9])])
while True:
    try:
        print(next(it))
    except StopIteration:
        break
