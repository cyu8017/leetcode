// LeetCode 3788 - Maximum Score Of A Split
// https://leetcode.com/problems/maximum-score-of-a-split/

class Solution {
    fun maximumScore(nums: IntArray): Long {
        var n = nums.size
        var suf = LongArray(n)
        suf[n - 1] = nums[n - 1]
        run {
            var i = n - 2
            while (i >= 0) {
                suf[i] = minOf(nums[i], suf[i + 1])
                i = i - 1
            }
        }
        var pre = 0
        var ans = Long.MIN_VALUE
        for (i in 0 until n - 1) {
            pre += nums[i]
            ans = maxOf(ans, pre - suf[i + 1])
        }
        return ans
    }
}
