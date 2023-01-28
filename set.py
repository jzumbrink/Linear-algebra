class Set:

    def __init__(self, finite_elements: set = {}, *intervals):
        self.finite_elements: set = finite_elements
        self.intervals = intervals

    def __iter__(self):
        return self.finite_elements.__iter__()

    def is_finite(self) -> bool:
        return len(self.intervals) == 0