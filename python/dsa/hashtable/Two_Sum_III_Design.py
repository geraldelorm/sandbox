class TwoSumThree:
    def __init__(self):
        self.bucket = collections.defaultdict(int)

    def add(self, value: int) -> None:
        self.bucket[value] += 1

    def find(self, value: int) -> bool:
        for key in self.bucket:
            comp = value - key
            if comp in self.bucket and (comp != key or self.bucket[key] > 1): 
                return True

        return False