// LeetCode 3291 - Minimum Number of Valid Strings to Form Target I
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/

class Solution {
    static class TrieNode {
        TrieNode[] next = TrieNode[26]
    }

    fun minValidStrings(words: Array<String>, target: String): Int {
        var n = target.length
        val inf = 1_000_000_000
        var dp = IntArray(n + 1)
        dp.fill(inf)
        dp[0] = 0
        TrieNode root = TrieNode()
        for (w in words) {
            TrieNode cur = root
            for (c in w.toCharArray()) {
                var ci = c - 'a'
                if (cur.next[ci] == null) cur.next[ci] = TrieNode()
                cur = cur.next[ci]
            }
        }
        for (i in 0 until n) {
            if (dp[i] == inf) continue
            TrieNode cur = root
            for (j in i until n) {
                var ci = target[j] - 'a'
                if (cur.next[ci] == null) break
                cur = cur.next[ci]
                if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1
            }
        }
        return if (dp[n] == inf) -1 else dp[n]
    }
}
