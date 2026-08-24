// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

class Solution {
    fun isSubstringPresent(s: String): Boolean {
        val st = Array(26) { BooleanArray(26) }
        for (i in 0 until s.length - 1) {
            st[s[i + 1] - 'a'][s[i] - 'a'] = true
        }
        for (i in 0 until s.length - 1) {
            if (st[s[i] - 'a'][s[i + 1] - 'a']) return true
        }
        return false
    }
}
