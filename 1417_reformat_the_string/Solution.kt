// LeetCode 1417 - Reformat The String
// https://leetcode.com/problems/reformat-the-string/

class Solution {
    fun reformat(s: String): String {
        val letters = ArrayList<Char>()
        val digits = ArrayList<Char>()
        for (c in s) {
            if (c.isLetter()) letters.add(c) else digits.add(c)
        }
        if (kotlin.math.abs(letters.size - digits.size) > 1) return ""
        var a = letters
        var b = digits
        if (b.size >= a.size) {
            a = digits
            b = letters
        }
        val answer = StringBuilder()
        for (i in a.indices) {
            answer.append(a[i])
            if (i < b.size) answer.append(b[i])
        }
        return answer.toString()
    }
}
