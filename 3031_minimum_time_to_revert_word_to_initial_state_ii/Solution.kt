// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

class Solution {
    class Hashing(word: String, bas: Long, mod_: Long) {
        val mod = mod_
        val p: LongArray
        val h: LongArray
        init {
            val n = word.length
            p = LongArray(n + 1)
            h = LongArray(n + 1)
            p[0] = 1
            for (i in 1..n) {
                p[i] = p[i - 1] * bas % mod
                h[i] = (h[i - 1] * bas + (word[i - 1] - 'a')) % mod
            }
        }
        fun query(l: Int, r: Int): Long {
            return (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod
        }
    }

    fun minimumTimeToInitialState(word: String, k: Int): Int {
        val hashing = Hashing(word, 13331, 998244353)
        val n = word.length
        var i = k
        while (i < n) {
            if (hashing.query(1, n - i) == hashing.query(i + 1, n)) return i / k
            i += k
        }
        return (n + k - 1) / k
    }
}
