// LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

class Solution {
    fun countValidSubarrays(nums: IntArray, x: Int): Int {
        var n = nums.size
        var ans = 0
        for (l in 0 until n) {
            var s = 0
            for (r in l until n) {
                s += nums[r]
                if (s % 10 == x) {
                    var t = Long.toString(s)
                    if (t[0] - '0' == x) ans++
                }
            }
        }
        return ans
    }
}
