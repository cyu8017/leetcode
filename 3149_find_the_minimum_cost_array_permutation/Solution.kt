// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

class Solution {
    private var nums: IntArray? = null
    private var n: Int = 0
    private var memo: Array<IntArray>? = null
    private var ans: MutableList<Int>? = null

    private fun absv(x: Int): Int {
        return if (x < 0) -x else x
    }

    private fun dfs(mask: Int, pre: Int): Int {
        if (mask == (1  shl  n) - 1) return absv(pre - nums[0])
        if (memo[mask][pre] != -1) return memo[mask][pre]
        var res = Int.MAX_VALUE
        for (cur in 1 until n) {
            if (((mask  shr  cur) & 1) == 0) {
                res = minOf(res, absv(pre - nums[cur]) + dfs(mask | (1  shl  cur), cur))
            }
        }
        return memo[mask][pre] = res
    }

    private fun g(mask: Int, pre: Int) {
        ans.add(pre)
        if (mask == (1  shl  n) - 1) return
        var res = dfs(mask, pre)
        for (cur in 1 until n) {
            if (((mask  shr  cur) & 1) == 0) {
                if (absv(pre - nums[cur]) + dfs(mask | (1  shl  cur), cur) == res) {
                    g(mask | (1  shl  cur), cur)
                    break
                }
            }
        }
    }

    fun findPermutation(nums: IntArray): IntArray {
        this.nums = nums
        this.n = nums.size
        this.memo = Array(1  shl  n) { IntArray(n) }
        for (row in memo) { row.fill(-1) }
        this.ans = ArrayList()
        g(1, 0)
        var out = IntArray(ans.size)
        for (i in 0 until ans.size) { out[i] = ans[i] }
        return out
    }
}
