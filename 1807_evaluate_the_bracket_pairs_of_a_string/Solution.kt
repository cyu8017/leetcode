// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

class Solution {
    fun evaluate(s: String, knowledge: Array<Array<String>>): String {
        val lookup = HashMap<String, String>()
        for (pair in knowledge) lookup[pair[0]] = pair[1]
        val result = StringBuilder()
        var i = 0
        while (i < s.length) {
            if (s[i] == '(') {
                val j = s.indexOf(')', i + 1)
                val key = s.substring(i + 1, j)
                result.append(lookup[key] ?: "?")
                i = j + 1
            } else {
                result.append(s[i])
                i++
            }
        }
        return result.toString()
    }
}
