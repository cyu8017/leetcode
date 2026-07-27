// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

class Solution {
    fun reformatNumber(number: String): String {
        var s = number.filter { it.isDigit() }
        val out = mutableListOf<String>()
        while (s.length > 4) {
            out.add(s.take(3))
            s = s.drop(3)
        }
        if (s.length == 4) {
            out.add(s.take(2))
            out.add(s.drop(2))
        } else if (s.isNotEmpty()) {
            out.add(s)
        }
        return out.joinToString("-")
    }
}
