// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

class Solution {
    fun maxDistinctElements(nums: IntArray, k: Int): Int {
        nums.sort()
        var ans = 0
        var prev = Long.MIN_VALUE / 2
        for (x in nums) {
            var cur = x - k
            if (cur <= prev) cur = prev + 1
            if (cur > x + k) continue
            ans = ans + 1
            prev = cur
        }
        return ans
    }
}
