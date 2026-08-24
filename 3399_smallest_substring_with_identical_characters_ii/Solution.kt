// LeetCode 3399 - Smallest Substring With Identical Characters II
// https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

class Solution {
    fun minLength(s: String, numOps: Int): Int {
        var n = s.length
        var lo = 1
        var hi = n
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (ok(s, n, numOps, mid)) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun ok(s: String, n: Int, numOps: Int, L: Int): Boolean {
        var ops = 0
        var i = 0
        while (i < n) {
            var j = i
            while (j < n && s[j] == s[i]) j++
            ops += (j - i) / (L + 1)
            i = j
            
        }
        return ops <= numOps
    }
}
