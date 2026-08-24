// LeetCode 3261 - Count Substrings That Satisfy K-Constraint II
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/

class Solution {
    fun countKConstraintSubstrings(s: String, k: Int, queries: Array<IntArray>): LongArray {
        var n = s.length
        var leftMost = IntArray(n)
        var z = 0
        var o = 0
        var L = 0
        for (R in 0 until n) {
            if (s[R] == '0') z++; else o++
            while (z > k && o > k) {
                if (s[L] == '0') z--; else o--
                L++
            }
            leftMost[R] = L
        }
        var pref = LongArray(n + 1)
        for (i in 0 until n) { pref[i + 1] = pref[i] + (i - leftMost[i] + 1) }
        var ans = LongArray(queries.size)
        for (qi in 0 until queries.size) {
            var l = queries[qi][0]
            var r = queries[qi][1]
            var lo = l
            var hi = r + 1
            while (lo < hi) {
                var mid = (lo + hi) / 2
                if (leftMost[mid] < l) lo = mid + 1
                else hi = mid
            }
            var res = 0
            if (lo > l) {
                var m = lo - l
                res += m * (m + 1) / 2
            }
            if (lo <= r) res += pref[r + 1] - pref[lo]
            ans[qi] = res
        }
        return ans
    }
}
