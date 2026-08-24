// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

class Solution {
    fun countPalindromes(s: String): Int {
        val mod = 1_000_000_007
        val n = s.length
        val pref = Array(n) { Array(10) { IntArray(10) } }
        val suf = Array(n) { Array(10) { IntArray(10) } }
        val cnt = IntArray(10)
        for (i in 0 until n) {
            if (i > 0) {
                for (a in 0 until 10) {
                    for (b in 0 until 10) pref[i][a][b] = pref[i - 1][a][b]
                }
            }
            val d = s[i] - '0'
            for (a in 0 until 10) pref[i][a][d] += cnt[a]
            cnt[d]++
        }
        cnt.fill(0)
        for (i in n - 1 downTo 0) {
            if (i + 1 < n) {
                for (a in 0 until 10) {
                    for (b in 0 until 10) suf[i][a][b] = suf[i + 1][a][b]
                }
            }
            val d = s[i] - '0'
            for (a in 0 until 10) suf[i][a][d] += cnt[a]
            cnt[d]++
        }
        var ans = 0
        for (i in 2 until n - 2) {
            for (a in 0 until 10) {
                for (b in 0 until 10) {
                    ans = ((ans + pref[i - 1][a][b].toLong() * suf[i + 1][a][b]) % mod).toInt()
                }
            }
        }
        return ans
    }
}
