// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/


class Solution {
    fun nextGreaterElement(n: Int): Int {
        val digits = n.toString().toCharArray()
        var i = digits.size - 2
        while (i >= 0 && digits[i] >= digits[i + 1]) i--
        if (i < 0) return -1
        var j = digits.size - 1
        while (digits[j] <= digits[i]) j--
        val tmp = digits[i]
        digits[i] = digits[j]
        digits[j] = tmp
        digits.reverse(i + 1, digits.size)
        val value = String(digits).toLong()
        return if (value > Int.MAX_VALUE) -1 else value.toInt()
    }
}
