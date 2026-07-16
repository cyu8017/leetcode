# LeetCode 1538

class ArrayReader:
    def __init__(self, nums):
        self.nums = nums
    def query(self, a, b, c, d):
        ones = self.nums[a] + self.nums[b] + self.nums[c] + self.nums[d]
        return 4 if ones in (0, 4) else 2 if ones in (1, 3) else 0
    def length(self):
        return len(self.nums)

class Solution:
    def guessMajority(self, reader):
        if isinstance(reader, list):
            reader = ArrayReader(reader)
        n = reader.length()
        first_four = reader.query(0, 1, 2, 3)
        shifted = reader.query(1, 2, 3, 4)
        same, different, different_index, later_different = 1, 0, -1, -1
        four_same = first_four == shifted
        if four_same:
            same += 1
        else:
            different += 1
            different_index = 4
        checks = [(0, 2, 3, 4), (0, 1, 3, 4), (0, 1, 2, 4)]
        for index, args in enumerate(checks, 1):
            if reader.query(*args) == shifted:
                same += 1
            else:
                different += 1
                different_index = index
        for i in range(5, n):
            i_same_as_four = reader.query(1, 2, 3, i) == shifted
            if i_same_as_four == four_same:
                same += 1
            else:
                different += 1
                different_index = i
                if later_different == -1:
                    later_different = i
        if same == different:
            return -1
        return 0 if same > different else (later_different if later_different != -1 else different_index)
