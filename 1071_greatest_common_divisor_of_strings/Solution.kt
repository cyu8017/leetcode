// LeetCode 1071 - Greatest Common Divisor of Strings
// https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution {
    fun gcdOfStrings(str1: String, str2: String): String {
        if (str1 + str2 != str2 + str1) return ""
        return str1.substring(0, gcd(str1.length, str2.length))
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
