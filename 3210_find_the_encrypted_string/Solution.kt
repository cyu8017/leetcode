// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

class Solution {
    fun getEncryptedString(s: String, k: Int): String {
        var n = s.length
        var cs = CharArray(n)
        for (i in 0 until n) { cs[i] = s[(i + k] % n) }
        return String(cs)
    }
}
