class Solution:
    def minOperations(self, nums1, nums2):
        if len(nums1) * 6 < len(nums2) or len(nums2) * 6 < len(nums1):
            return -1
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s1 < s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        diff = s1 - s2
        gains = sorted([x - 1 for x in nums1] + [6 - x for x in nums2], reverse=True)
        ops = 0
        for gain in gains:
            if diff <= 0:
                break
            diff -= gain
            ops += 1
        return ops if diff <= 0 else -1
