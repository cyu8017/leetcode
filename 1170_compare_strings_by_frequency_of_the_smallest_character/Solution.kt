// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

class Solution {
    fun numSmallerByFrequency(queries: Array<String>, words: Array<String>): IntArray {
        val freqs = IntArray(words.size) { f(words[it]) }
        freqs.sort()
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val fq = f(queries[i])
            var lo = 0
            var hi = freqs.size
            while (lo < hi) {
                val mid = (lo + hi) / 2
                if (freqs[mid] <= fq) lo = mid + 1 else hi = mid
            }
            ans[i] = freqs.size - lo
        }
        return ans
    }

    private fun f(s: String): Int {
        var min = 'z'
        for (c in s) if (c < min) min = c
        var cnt = 0
        for (c in s) if (c == min) cnt++
        return cnt
    }
}
