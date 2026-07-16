class Solution:
    def minOperations(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        if n < m:
            nums1, nums2 = nums2, nums1
            n, m = m, n
        total = sum(nums1) + sum(nums2)
        if total % n:
            return -1
        target = total // n
        diff = [target - x for x in nums2 if x <= target]
        if len(diff) != m:
            return -1
        return sum(diff)
