// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

class Solution {
    fun hasSpecialSubstring(s: String, k: Int): Boolean {
        var n = s.length
        var i = 0
        while (i + k <= n) {
            var ok = true
            for (j in i + 1 until i + k) {
                if (s[j] != s[i]) { ok = false; break; }
            }
            if (!ok) continue
            if (i > 0 && s[i - 1] == s[i]) continue
            if (i + k < n && s[i + k] == s[i]) continue
            return true
            i = i + 1
        }
        return false
    }
}
