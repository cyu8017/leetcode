// LeetCode 3003 - Maximize the Number of Partitions After Operations
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

class Solution {
    private lateinit var s: String
    private var k = 0
    private var n = 0
    private lateinit var memo: HashMap<Long, Int>

    private fun popcount(x0: Int): Int {
        var x = x0
        var c = 0
        while (x != 0) {
            c += x and 1
            x = x shr 1
        }
        return c
    }

    private fun key(i: Int, cur: Int, t: Int): Long {
        return (i.toLong() shl 32) or (cur.toLong() shl 1) or t.toLong()
    }

    private fun dfs(i: Int, cur: Int, t: Int): Int {
        if (i >= n) return 1
        val kkey = key(i, cur, t)
        memo[kkey]?.let { return it }
        val v = 1 shl (s[i] - 'a')
        var nxt = cur or v
        var ans = if (popcount(nxt) > k) dfs(i + 1, v, t) + 1 else dfs(i + 1, nxt, t)
        if (t > 0) {
            for (j in 0 until 26) {
                nxt = cur or (1 shl j)
                ans = if (popcount(nxt) > k) {
                    maxOf(ans, dfs(i + 1, 1 shl j, 0) + 1)
                } else {
                    maxOf(ans, dfs(i + 1, nxt, 0))
                }
            }
        }
        memo[kkey] = ans
        return ans
    }

    fun maxPartitionsAfterOperations(s: String, k: Int): Int {
        this.s = s
        this.k = k
        this.n = s.length
        this.memo = HashMap()
        return dfs(0, 0, 1)
    }
}
