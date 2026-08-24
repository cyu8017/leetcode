// LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

class Solution {
    fun getWordsInLongestSubsequence(words: Array<String>, groups: IntArray): MutableList<String> {
        var n = words.size
        var dp = IntArray(n)
        var prev = IntArray(n)
        for (i in 0 until n) {
            dp[i] = 1
            prev[i] = -1
        }
        var best = 1
        var bestI = 0
        for (i in 0 until n) {
            for (j in 0 until i) {
                if (groups[i] != groups[j] && hamming(words[i], words[j]) == 1 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1
                    prev[i] = j
                }
            }
            if (dp[i] > best) {
                best = dp[i]
                bestI = i
            }
        }
        var path = ArrayList<String>()
        run {
            var i = bestI
            while (i != -1) {
                path.add(words[i])
                i = prev[i]
            }
        }
        path.reverse()
        return path
    }

    private fun hamming(a: String, b: String): Int {
        if (a.length != b.length) return 100
        var d = 0
        for (i in 0 until a.length) { if (a[i] != b[i]) d++ }
        return d
    }
}
