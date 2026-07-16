// LeetCode 0066 - Plus One
// https://leetcode.com/problems/plus-one/

class Solution {
    fun plusOne(digits: IntArray): IntArray {
        for (i in digits.indices.reversed()) {
            if (digits[i] < 9) {
                digits[i]++
                return digits
            }
            digits[i] = 0
        }

        return IntArray(digits.size + 1).also { it[0] = 1 }
    }
}
