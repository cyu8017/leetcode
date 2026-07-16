// LeetCode 0043 - Multiply Strings
// https://leetcode.com/problems/multiply-strings/

class Solution {
    fun multiply(num1: String, num2: String): String {
        if (num1 == "0" || num2 == "0") {
            return "0"
        }

        val positions = IntArray(num1.length + num2.length)

        for (i in num1.length - 1 downTo 0) {
            for (j in num2.length - 1 downTo 0) {
                val product = (num1[i] - '0') * (num2[j] - '0')
                val low = i + j + 1
                val high = i + j
                val total = product + positions[low]
                positions[low] = total % 10
                positions[high] += total / 10
            }
        }

        val start = positions.indexOfFirst { it != 0 }.let { if (it == -1) positions.size else it }
        return if (start == positions.size) {
            "0"
        } else {
            positions.drop(start).joinToString("")
        }
    }
}
