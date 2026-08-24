// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

class Solution {
    fun findLatestTime(s: String): String {
        var h = 11
        while (true) {
            for (m in 59 downTo 0) {
                var t = String.format("%02d:%02d", h, m)
                var ok = true
                for (i in 0 until 5) {
                    if (s[i] != '?' && s[i] != t[i]) {
                        ok = false
                        break
                    }
                }
                if (ok) return t
            }
            h--
        }
    }
}
