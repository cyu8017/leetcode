// LeetCode 1062 - Longest Repeating Substring
// https://leetcode.com/problems/longest-repeating-substring/

class Solution {
    fun longestRepeatingSubstring(s: String): Int {
        val n = s.length
        var lo = 1
        var hi = n - 1
        var ans = 0
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            if (hasDup(s, mid)) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }

    private fun hasDup(s: String, length: Int): Boolean {
        val seen = HashSet<String>()
        for (i in 0..s.length - length) {
            val sub = s.substring(i, i + length)
            if (!seen.add(sub)) return true
        }
        return false
    }
}
