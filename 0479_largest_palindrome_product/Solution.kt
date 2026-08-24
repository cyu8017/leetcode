// LeetCode 0479 - Largest Palindrome Product
// https://leetcode.com/problems/largest-palindrome-product/

class Solution {
    fun largestPalindrome(n: Int): Int {
        if (n == 1) {
            return 9
        }
        val upper = Math.pow(10.0, n.toDouble()).toInt() - 1
        val lower = Math.pow(10.0, (n - 1).toDouble()).toInt()
        for (first in upper downTo lower) {
            val firstString = first.toString()
            val candidate = (firstString + firstString.reversed()).toLong()
            var factor = upper
            while (factor.toLong() * factor >= candidate) {
                if (candidate % factor == 0L) {
                    val partner = (candidate / factor).toInt()
                    if (partner in lower..upper) {
                        return (candidate % 1337).toInt()
                    }
                }
                factor--
            }
        }
        return 0
    }
}
