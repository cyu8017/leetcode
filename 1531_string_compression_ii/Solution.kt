// LeetCode 1531 - String Compression II
// https://leetcode.com/problems/string-compression-ii/

class Solution {
    private lateinit var s: String
    private lateinit var memo: Array<IntArray>

    fun getLengthOfOptimalCompression(s: String, k: Int): Int {
        this.s = s
        memo = Array(s.length + 1) { IntArray(k + 1) { -1 } }
        return dp(0, k)
    }

    private fun dp(index: Int, remaining: Int): Int {
        if (remaining < 0) return 1_000_000_000
        if (index == s.length || s.length - index <= remaining) return 0
        if (memo[index][remaining] != -1) return memo[index][remaining]
        var answer = dp(index + 1, remaining - 1)
        var same = 0
        var removed = 0
        for (j in index until s.length) {
            if (s[j] == s[index]) {
                same++
                val encoded = 1 + (if (same >= 2) 1 else 0) + (if (same >= 10) 1 else 0) + (if (same >= 100) 1 else 0)
                answer = minOf(answer, encoded + dp(j + 1, remaining - removed))
            } else {
                removed++
                if (removed > remaining) break
            }
        }
        memo[index][remaining] = answer
        return answer
    }
}
