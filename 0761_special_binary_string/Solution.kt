// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

class Solution {
    fun makeLargestSpecial(s: String): String {
        val parts = ArrayList<String>()
        var balance = 0
        var start = 0
        for (i in s.indices) {
            balance += if (s[i] == '1') 1 else -1
            if (balance == 0) {
                parts.add("1" + makeLargestSpecial(s.substring(start + 1, i)) + "0")
                start = i + 1
            }
        }
        parts.sortDescending()
        val result = StringBuilder()
        for (part in parts) result.append(part)
        return result.toString()
    }
}
