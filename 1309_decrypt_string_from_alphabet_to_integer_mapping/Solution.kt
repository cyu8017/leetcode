// LeetCode 1309 - Decrypt String from Alphabet to Integer Mapping
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution {
    fun freqAlphabets(s: String): String {
        val answer = mutableListOf<Char>()
        var i = s.length - 1
        while (i >= 0) {
            if (s[i] == '#') {
                answer.add(('a'.code + s.substring(i - 2, i).toInt() - 1).toChar())
                i -= 3
            } else {
                answer.add(('a'.code + (s[i] - '0') - 1).toChar())
                i -= 1
            }
        }
        return answer.asReversed().joinToString("")
    }
}
