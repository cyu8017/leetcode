// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

class Solution {
    fun getSubarrayBeauty(nums: IntArray, k: Int, x: Int): IntArray {
        val freq = IntArray(101)
        val ans = IntArray(nums.size - k + 1)
        for (i in nums.indices) {
            freq[nums[i] + 50]++
            if (i >= k) freq[nums[i - k] + 50]--
            if (i >= k - 1) {
                var need = x
                var `val` = 0
                for (j in 0 until 50) {
                    need -= freq[j]
                    if (need <= 0) {
                        `val` = j - 50
                        break
                    }
                }
                ans[i - k + 1] = `val`
            }
        }
        return ans
    }
}
