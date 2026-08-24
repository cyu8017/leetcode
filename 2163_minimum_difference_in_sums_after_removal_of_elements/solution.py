# LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

from typing import List
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        left = [0] * (len(nums))
        right = [0] * (len(nums))
        hmax = []
        def pushMax(x):
            hmax.append(x)
            i = len(hmax) - 1
            while i > 0:
                p = (i - 1) >> 1
                if hmax[p] >= hmax[i]:
                    break
                hmax[p], hmax[i] = hmax[i], hmax[p]
                i = p

        def popMax():
            top = hmax[0]
            last = hmax.pop()
            if hmax:
                hmax[0] = last
                i = 0
                while True:
                    l = i * 2 + 1
                    r = l + 1
                    s = i
                    if l < len(hmax) and hmax[l] > hmax[s]:
                        s = l
                    if r < len(hmax) and hmax[r] > hmax[s]:
                        s = r
                    if s == i:
                        break
                    hmax[s], hmax[i] = hmax[i], hmax[s]
                    i = s
            return top

        sum = 0
        for i in range(n):
            pushMax(nums[i])
            sum += nums[i]
        left[n - 1] = sum
        for i in range(n, 2 * n):
            pushMax(nums[i])
            sum += nums[i]
            sum -= popMax()
            left[i] = sum
        hmin = []
        def pushMin(x):
            hmin.append(x)
            i = len(hmin) - 1
            while i > 0:
                p = (i - 1) >> 1
                if hmin[p] <= hmin[i]:
                    break
                hmin[p], hmin[i] = hmin[i], hmin[p]
                i = p

        def popMin():
            top = hmin[0]
            last = hmin.pop()
            if hmin:
                hmin[0] = last
                i = 0
                while True:
                    l = i * 2 + 1
                    r = l + 1
                    s = i
                    if l < len(hmin) and hmin[l] < hmin[s]:
                        s = l
                    if r < len(hmin) and hmin[r] < hmin[s]:
                        s = r
                    if s == i:
                        break
                    hmin[s], hmin[i] = hmin[i], hmin[s]
                    i = s
            return top

        sum = 0
        for i in range(len(nums) - 1, (2 * n) - 1, -1):
            pushMin(nums[i])
            sum += nums[i]
        right[2 * n] = sum
        for i in range(2 * n - 1, (n) - 1, -1):
            pushMin(nums[i])
            sum += nums[i]
            sum -= popMin()
            right[i] = sum
        ans = left[n - 1] - right[n]
        for i in range(n, 2 * n):
            ans = min(ans, left[i] - right[i + 1])
        return ans
