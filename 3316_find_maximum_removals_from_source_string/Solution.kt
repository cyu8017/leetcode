// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

class Solution {
    fun maxRemovals(source: String, pattern: String, targetIndices: IntArray): Int {
        val n = source.length
        var lo = 0
        var hi = targetIndices.size
        while (lo < hi) {
            val mid = (lo + hi + 1) / 2
            if (ok(mid, source, pattern, targetIndices, n)) lo = mid
            else hi = mid - 1
        }
        return lo
    }

    private fun ok(removeFirst: Int, source: String, pattern: String, targetIndices: IntArray, n: Int): Boolean {
        val mark = BooleanArray(n)
        for (i in 0 until removeFirst) mark[targetIndices[i]] = true
        var j = 0
        var i = 0
        while (i < n && j < pattern.length) {
            if (!mark[i] && source[i] == pattern[j]) j++
            i++
        }
        return j == pattern.length
    }
}
