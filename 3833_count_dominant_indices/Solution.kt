// LeetCode 3833 - Count Dominant Indices
// https://leetcode.com/problems/count-dominant-indices/

class Solution {
    fun dominantIndices(nums: IntArray): Int {
        var n = nums.size
        var ans = 0
        var suf = nums[n - 1]
        for (i in n - 2 downTo 0) {
            if (nums[i] * (n - i - 1) > suf) ans++
            suf += nums[i]
        }
        return ans
    }
}
