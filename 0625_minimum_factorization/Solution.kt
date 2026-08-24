// LeetCode 0625 - Minimum Factorization
// https://leetcode.com/problems/minimum-factorization/


class Solution {
    fun smallestFactorization(num: Int): Int {
        if (num < 10) return num
        val digits = ArrayList<Int>()
        var n = num
        for (d in 9 downTo 2) {
            while (n % d == 0) {
                digits.add(d)
                n /= d
            }
        }
        if (n != 1) return 0
        digits.sort()
        var result = 0L
        for (d in digits) {
            result = result * 10 + d
            if (result > Int.MAX_VALUE) return 0
        }
        return result.toInt()
    }
}
