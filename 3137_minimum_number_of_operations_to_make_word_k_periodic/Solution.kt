// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

class Solution {
    fun minimumOperationsToMakeKPeriodic(word: String, k: Int): Int {
        var cnt = HashMap<String, Int>()
        var n = word.length, mx = 0
        var i = 0
        while (i < n) {
            var s = word.substring(i, i + k)
            var v = cnt.getOrDefault(s, 0) + 1
            cnt[s] = v
            mx = maxOf(mx, v)
            i += k
        }
        return n / k - mx
    }
}
