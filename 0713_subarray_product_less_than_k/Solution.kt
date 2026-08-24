// LeetCode 0713 - Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/

class Solution {
    fun numSubarrayProductLessThanK(nums: IntArray, k: Int): Int {
        if (k <= 1) return 0
        var product = 1
        var left = 0
        var ans = 0
        for (right in 0 until nums.size) {
            product *= nums[right]
            while (product >= k) product /= nums[left++]
            ans += right - left + 1
        }
        return ans
    }
}
