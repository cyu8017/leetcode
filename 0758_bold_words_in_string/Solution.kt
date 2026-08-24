// LeetCode 0758 - Bold Words in String
// https://leetcode.com/problems/bold-words-in-string/

class Solution {
    fun boldWords(words: Array<String>, s: String): String {
        var n = s.length
        var bold = BooleanArray(n)
        for (word in words) {
            var start = s.indexOf(word)
            while (start >= 0) {
                for (i in start until start + word.length) { bold[i] = true }
                start = s.indexOf(word, start + 1)
            }
        }
        var parts = StringBuilder()
        var i2 = 0
        while (i2 < n) {
            if (bold[i2]) {
                parts.append("**")
                while (i2 < n && bold[i2]) parts.append(s[i2++])
                parts.append("**")
            } else parts.append(s[i2++])
        }
        return parts.toString()
    }
}
