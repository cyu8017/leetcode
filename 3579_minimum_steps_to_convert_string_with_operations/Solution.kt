// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

class Solution {
    var word1: String? = null
    var word2: String? = null

    fun calc(l: Int, r: Int, rev: Boolean): Int {
        var cnt = Array(26) { IntArray(26) }
        var res = 0
        for (i in l..r) {
            var j = if (rev) r - (i - l) else i
            var a = word1[j] - 'a'
            var b = word2[i] - 'a'
            if (a != b) {
                if (cnt[b][a] > 0) cnt[b][a]--
                else {
                    cnt[a][b]++
                    res = res + 1
                }
            }
        }
        return res
    }

    fun minOperations(word1: String, word2: String): Int {
        this.word1 = word1
        this.word2 = word2
        var n = word1.length
        var f = IntArray(n + 1)
        java.util.f.fill(Int.MAX_VALUE / 2)
        f[0] = 0
        for (i in 1..n) {
            for (j in 0 until i) {
                var a = calc(j, i - 1, false)
                var b = 1 + calc(j, i - 1, true)
                f[i] = minOf(f[i], f[j] + minOf(a, b))
            }
        }
        return f[n]
    }
}
