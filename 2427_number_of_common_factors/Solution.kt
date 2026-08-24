// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

class Solution {
    fun commonFactors(a: Int, b: Int): Int {
        val g = gcd(a, b)
        var ans = 0
        var i = 1
        while (i * i <= g) {
            if (g % i == 0) {
                ans++
                if (i * i != g) ans++
            }
            i++
        }
        return ans
    }

    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }
}
