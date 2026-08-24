// LeetCode 2165 - Smallest Value of the Rearranged Number
// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

class Solution {
    fun smallestNumber(num: Long): Long {
        var neg: Boolean = num < 0
        if (neg) num = -num
        if (num == 0) return 0
        var digits = mutableListOf()
        while (num > 0) { digits.add(('0' + num % 10)); num /= 10; }
        if (neg) {
            digits.sort(Collections.reverseOrder())
            var ans: Long = 0
            for (d in digits) ans = ans * 10 + (d - '0')
            return -ans
        }
        digits.sort()
        if (digits.get(0) == '0') {
            for (i in 1 until digits.size) {
                if (digits.get(i) != '0') {
                    var t: Char = digits.get(0); digits.set(0, digits.get(i)); digits.set(i, t)
                    break
                }
            }
        }
        var res: Long = 0
        for (d in digits) res = res * 10 + (d - '0')
        return res
    }
}
