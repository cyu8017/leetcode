// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

class Solution {
    private var k: Int = 0
    private var f: MutableMap<Long, Int>? = null

    private fun dfs(i: Long, j: Int, jump: Int): Int {
        if (i > k + 1) return 0
        var key = (i  shl  32) | (jump  shl  1) | j
        var cached = f[key]
        if (cached != null) return cached
        var ans = 0
        if (i == k) ans++
        if (i > 0 && j == 0) ans += dfs(i - 1, 1, jump)
        ans += dfs(i + (1L  shl  jump), 0, jump + 1)
        f[key] = ans
        return ans
    }

    fun waysToReachStair(k: Int): Int {
        this.k = k
        this.f = HashMap()
        return dfs(1, 0, 0)
    }
}
