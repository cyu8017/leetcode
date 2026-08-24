// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

class Solution {
    fun splitNum(num: Int): Int {
        var n = num
        val digits = ArrayList<Int>()
        while (n > 0) {
            digits.add(n % 10)
            n /= 10
        }
        digits.sort()
        var a = 0
        var b = 0
        for (i in digits.indices) {
            if (i % 2 == 0) a = a * 10 + digits[i]
            else b = b * 10 + digits[i]
        }
        return a + b
    }
}
