// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

class Solution {
    fun sumDigitDifferences(nums: IntArray): Long {
        var n = nums.size
        var m = kotlin.math.floor(Math.log10(nums[0])) + 1
        var ans = 0
        var vals = nums.clone()
        for (k in 0 until m) {
            var cnt = IntArray(10)
            for (i in 0 until n) {
                cnt[vals[i] % 10]++
                vals[i] /= 10
            }
            for (v in cnt) { ans += 1L * v * (n - v) }
        }
        return ans / 2
    }
}
