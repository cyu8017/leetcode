// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

class Solution {
    fun kthSmallestSubarraySum(nums: IntArray, k: Int): Int {
        fun count(limit: Int): Int {
            var total = 0
            var left = 0
            var ans = 0
            for (right in nums.indices) {
                total += nums[right]
                while (total > limit) {
                    total -= nums[left]
                    left++
                }
                ans += right - left + 1
            }
            return ans
        }
        var lo = nums.minOrNull()!!
        var hi = nums.sum()
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (count(mid) >= k) hi = mid else lo = mid + 1
        }
        return lo
    }
}
