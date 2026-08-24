// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

class Solution {
    fun stringHash(s: String, k: Int): String {
        val outSb = StringBuilder(s.length / k)
        var i = 0
        while (i < s.length) {
            var sum = 0
            for (j in i until i + k) sum += s[j] - 'a'
            outSb.append(('a'.code + sum % 26).toChar())
            i += k
        }
        return outSb.toString()
    }
}
