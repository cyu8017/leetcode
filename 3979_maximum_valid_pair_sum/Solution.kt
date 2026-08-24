// LeetCode 3979 - Maximum Valid Pair Sum
// https://leetcode.com/problems/maximum-valid-pair-sum/

class Solution {
    fun maxValidPairSum(nums: IntArray, k: Int): Int {
        var ans = 0
        var x = 0
        for (j in k until nums.size) {
            var y = nums[j]
            x = maxOf(x, nums[j - k])
            ans = maxOf(ans, x + y)
        }
        return ans
    }
}
