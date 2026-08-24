// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

class Solution {
    fun sameEndSubstringCount(s: String, queries: Array<IntArray>): IntArray {
        val n = s.length
        val pref = Array(n + 1) { IntArray(26) }
        for (i in 0 until n) {
            pref[i + 1] = pref[i].copyOf()
            pref[i + 1][s[i] - 'a']++
        }
        val ans = IntArray(queries.size)
        for (qi in queries.indices) {
            val l = queries[qi][0]
            val r = queries[qi][1]
            var total = 0
            for (c in 0 until 26) {
                val cnt = pref[r + 1][c] - pref[l][c]
                total += cnt * (cnt + 1) / 2
            }
            ans[qi] = total
        }
        return ans
    }
}
