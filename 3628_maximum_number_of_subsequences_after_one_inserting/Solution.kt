// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

class Solution {
    private fun calc(s: String, t: String): Long {
        var cnt = 0
        var a = 0
        for (c in s.toCharArray()) {
            if (c == t[1]) cnt += a
            if (c == t[0]) a++
        }
        return cnt
    }

    fun numOfSubsequences(s: String): Long {
        var l = 0
        var r = 0
        for (char c : s.toCharArray())
            if (c == 'T') r++
        var ans = 0
        var mx = 0
        for (c in s.toCharArray()) {
            if (c == 'T') r--
            if (c == 'C') ans += l * r
            if (c == 'L') l++
            mx = maxOf(mx, l * r)
        }
        mx = maxOf(mx, maxOf(calc(s, "LC"), calc(s, "CT")))
        return ans + mx
    }
}
