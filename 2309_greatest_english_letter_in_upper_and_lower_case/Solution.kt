// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution {
    fun greatestLetter(s: String): String {
        val lower = BooleanArray(26)
        val upper = BooleanArray(26)
        for (c in s) {
            if (c in 'a'..'z') lower[c - 'a'] = true
            else if (c in 'A'..'Z') upper[c - 'A'] = true
        }
        for (i in 25 downTo 0) {
            if (lower[i] && upper[i]) return ('A' + i).toString()
        }
        return ""
    }
}
