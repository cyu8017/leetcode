// LeetCode 0306 - Additive Number
// https://leetcode.com/problems/additive-number/

class Solution {
    fun isAdditiveNumber(num: String): Boolean {
        for (firstEnd in 1 until num.length) {
            for (secondEnd in firstEnd + 1 until num.length) {
                if (valid(num, num.substring(0, firstEnd), num.substring(firstEnd, secondEnd), secondEnd)) {
                    return true
                }
            }
        }
        return false
    }

    private fun valid(num: String, first: String, second: String, start: Int): Boolean {
        if ((first.length > 1 && first[0] == '0') || (second.length > 1 && second[0] == '0')) {
            return false
        }
        var currentStart = start
        var currentFirst = first
        var currentSecond = second
        while (currentStart < num.length) {
            val total = addStrings(currentFirst, currentSecond)
            if (!num.startsWith(total, currentStart)) {
                return false
            }
            currentFirst = currentSecond
            currentSecond = total
            currentStart += total.length
        }
        return true
    }

    private fun addStrings(left: String, right: String): String {
        return (left.toLong() + right.toLong()).toString()
    }
}
