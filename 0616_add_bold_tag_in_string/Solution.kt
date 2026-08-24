// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/


class Solution {
    fun addBoldTag(s: String, words: Array<String>): String {
        val n = s.length
        val bold = BooleanArray(n)
        for (word in words) {
            var start = s.indexOf(word)
            while (start >= 0) {
                for (i in start until start + word.length) bold[i] = true
                start = s.indexOf(word, start + 1)
            }
        }
        val sb = StringBuilder()
        var i = 0
        while (i < n) {
            if (!bold[i]) {
                sb.append(s[i])
                i++
            } else {
                sb.append("<b>")
                while (i < n && bold[i]) {
                    sb.append(s[i])
                    i++
                }
                sb.append("</b>")
            }
        }
        return sb.toString()
    }
}
