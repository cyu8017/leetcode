// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

class Solution {
    fun countDifferentSubsequenceGCDs(nums: IntArray): Int {
        val maxVal = nums.maxOrNull()!!
        val present = BooleanArray(maxVal + 1)
        for (num in nums) present[num] = true

        var ans = 0
        for (g in 1..maxVal) {
            var has = false
            var gcdVal = 0
            var multiple = g
            while (multiple <= maxVal) {
                if (present[multiple]) {
                    has = true
                    gcdVal = gcd(gcdVal, multiple / g)
                    if (gcdVal == 1) break
                }
                multiple += g
            }
            if (has && gcdVal == 1) ans++
        }
        return ans
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
