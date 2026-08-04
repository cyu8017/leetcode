// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

class Solution {
    fun sequentialDigits(low: Int, high: Int): List<Int> {
        val digits = "123456789"
        val answer = mutableListOf<Int>()
        for (length in 2..9) {
            for (start in 0..9 - length) {
                val value = digits.substring(start, start + length).toInt()
                if (value in low..high) answer.add(value)
            }
        }
        return answer
    }
}
