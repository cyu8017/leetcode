// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

class Solution {
    private val MOD: Int = 1_000_000_007
    private var nums: IntArray? = null
    private var memo: Array<IntArray>? = null

    fun specialPerm(nums: IntArray): Int {
        this.nums = nums
        var n = nums.size
        memo = Array(1  shl  n) { IntArray(n) }
        for (row in memo) { row.fill(-1) }
        var ans = 0
        for (i in 0 until n) { ans = (ans + dfs(1  shl  i, i)) % MOD }
        return ans
    }

    private fun dfs(mask: Int, last: Int): Int {
        if (mask == (1  shl  nums.size) - 1) return 1
        if (memo[mask][last] != -1) return memo[mask][last]
        var res = 0
        for (i in 0 until nums.size) {
            if ((mask & (1  shl  i)) != 0) continue
            if (nums[i] % nums[last] == 0 || nums[last] % nums[i] == 0)
                res = (res + dfs(mask | (1  shl  i), i)) % MOD
        }
        return memo[mask][last] = res
    }
}
