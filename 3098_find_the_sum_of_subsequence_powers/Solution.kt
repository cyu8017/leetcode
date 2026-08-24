// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

class Solution {
    private val MOD: Int = 1_000_000_007
    private var nums: IntArray? = null
    private var n: Int = 0
    private var f: MutableMap<Long, Int>? = null

    private fun dfs(i: Int, j: Int, kk: Int, mi: Int): Int {
        if (i >= n) return if (kk == 0) mi else 0
        if (n - i < kk) return 0
        var key = (mi  shl  18) | (i  shl  12) | (j  shl  6) | kk
        var cached = f[key]
        if (cached != null) return cached
        var ans = dfs(i + 1, j, kk, mi)
        if (j == n) ans = (ans + dfs(i + 1, i, kk - 1, mi)) % MOD
        else ans = (ans + dfs(i + 1, i, kk - 1, minOf(mi, nums[i] - nums[j]))) % MOD
        f[key] = ans
        return ans
    }

    fun sumOfPowers(nums: IntArray, k: Int): Int {
        nums.sort()
        this.nums = nums
        this.n = nums.size
        this.f = HashMap()
        return dfs(0, n, k, Int.MAX_VALUE)
    }
}
