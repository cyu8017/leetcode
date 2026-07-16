# LeetCode 0327 - Count of Range Sum
# https://leetcode.com/problems/count-of-range-sum/

from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        temp = [0] * len(prefix)

        def merge_sort(left: int, right: int) -> int:
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)
            start = end = mid + 1
            for index in range(left, mid + 1):
                while start <= right and prefix[start] - prefix[index] < lower:
                    start += 1
                while end <= right and prefix[end] - prefix[index] <= upper:
                    end += 1
                count += end - start
            temp_left, temp_right, write = left, mid + 1, left
            while temp_left <= mid and temp_right <= right:
                if prefix[temp_left] <= prefix[temp_right]:
                    temp[write] = prefix[temp_left]
                    temp_left += 1
                else:
                    temp[write] = prefix[temp_right]
                    temp_right += 1
                write += 1
            while temp_left <= mid:
                temp[write] = prefix[temp_left]
                temp_left += 1
                write += 1
            while temp_right <= right:
                temp[write] = prefix[temp_right]
                temp_right += 1
                write += 1
            prefix[left : right + 1] = temp[left : right + 1]
            return count

        return merge_sort(0, len(prefix) - 1)
