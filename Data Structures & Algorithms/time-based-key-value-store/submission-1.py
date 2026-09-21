class TimeMap:

    def __init__(self):
        self.tbl = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tbl:
            self.tbl[key] = []
        self.tbl[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        op = ""
        values = self.tbl.get(key, [])
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                op = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return op

