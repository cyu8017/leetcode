// LeetCode 3982 - Sum of Integers with Maximum Digit Range
// https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

class Solution {
    fun maxDigitRange(nums: IntArray): Int {
        var mx = 0
        var ans = 0
        for (x in nums) {
            var a = 10
            var b = 0
            var y = x
            while (y > 0) {
                var v = y % 10
                a = minOf(a, v)
                b = maxOf(b, v)
                y /= 10
            }
            var r = b - a
            if (mx < r) {
                mx = r
                ans = x
            } else if (mx == r) {
                ans += x
            }
        }
        return ans
    }
}
