// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

class Solution {
    fun alternatingSum(nums: IntArray): Int {
        var ans = 0
        for (i in 0 until nums.size) {
            if (i % 2 == 0) ans += nums[i]
            else ans -= nums[i]
        }
        return ans
    }
}
