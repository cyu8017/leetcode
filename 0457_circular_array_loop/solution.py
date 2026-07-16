# LeetCode 0457 - Circular Array Loop
# https://leetcode.com/problems/circular-array-loop/


class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        length = len(nums)

        def next_index(index: int) -> int:
            return (index + nums[index]) % length

        for start in range(length):
            if nums[start] == 0:
                continue
            forward = nums[start] > 0
            slow = fast = start
            while True:
                slow = next_index(slow)
                fast = next_index(next_index(fast))
                if (
                    nums[slow] * (1 if forward else -1) <= 0
                    or nums[fast] * (1 if forward else -1) <= 0
                    or nums[next_index(fast)] * (1 if forward else -1) <= 0
                ):
                    break
                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

            index = start
            value = nums[start]
            while nums[index] * value > 0:
                nums[index] = 0
                index = next_index(index)

        return False
