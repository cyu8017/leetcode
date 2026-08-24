// LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

class Solution {
    fun countWays(word1: String, word2: String, target: String): Int {
        val mod = 1000000007
        val n1 = word1.length
        val n2 = word2.length
        val size = (n1 + 1) * (n2 + 1) * 4
        var dp = IntArray(size)
        var next = IntArray(size)
        dp[index(0, 0, 0, n2)] = 1
        for (ti in target.indices) {
            val ch = target[ti]
            next.fill(0)
            for (j in 0..n2) {
                val prefix = IntArray(4)
                for (a in 0 until n1) {
                    for (mask in 0 until 4) {
                        prefix[mask] += dp[index(a, j, mask, n2)]
                        if (prefix[mask] >= mod) prefix[mask] -= mod
                    }
                    if (word1[a] == ch) {
                        for (mask in 0 until 4) {
                            val at = index(a + 1, j, mask or 1, n2)
                            next[at] += prefix[mask]
                            if (next[at] >= mod) next[at] -= mod
                        }
                    }
                }
            }
            for (i in 0..n1) {
                val prefix = IntArray(4)
                for (b in 0 until n2) {
                    for (mask in 0 until 4) {
                        prefix[mask] += dp[index(i, b, mask, n2)]
                        if (prefix[mask] >= mod) prefix[mask] -= mod
                    }
                    if (word2[b] == ch) {
                        for (mask in 0 until 4) {
                            val at = index(i, b + 1, mask or 2, n2)
                            next[at] += prefix[mask]
                            if (next[at] >= mod) next[at] -= mod
                        }
                    }
                }
            }
            val tmp = dp
            dp = next
            next = tmp
        }
        var answer = 0
        for (i in 0..n1) {
            for (j in 0..n2) {
                answer += dp[index(i, j, 3, n2)]
                if (answer >= mod) answer -= mod
            }
        }
        return answer
    }

    private fun index(i: Int, j: Int, mask: Int, n2: Int): Int {
        return ((i * (n2 + 1) + j) * 4) + mask
    }
}
