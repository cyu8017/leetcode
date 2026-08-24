// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

class Solution {
    fun countBeautifulPairs(nums: IntArray): Int {
        var ans = 0
        val freq = IntArray(10)
        for (x in nums) {
            val last = x % 10
            for (d in 1..9) {
                if (freq[d] > 0 && gcd(d, last) == 1) ans += freq[d]
            }
            freq[firstDigit(x)]++
        }
        return ans
    }

    private fun firstDigit(x: Int): Int {
        var v = x
        while (v >= 10) v /= 10
        return v
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val t = x % y
            x = y
            y = t
        }
        return x
    }
}
