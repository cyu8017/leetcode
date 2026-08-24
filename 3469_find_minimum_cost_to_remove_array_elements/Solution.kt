// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

class Solution {
    private val memo = HashMap<Long, Int>()
    private var nums: IntArray? = null
    private var n: Int = 0

    private fun max2(a: Int, b: Int): Int { return if (a > b) a else b }
    private fun min3(a: Int, b: Int, c: Int): Int { return minOf(a, minOf(b, c)) }

    private fun key(i: Int, prev: Int): Long { return (i  shl  32) | (prev & 0xffffffffL) }

    private fun dfs(i: Int, prev: Int): Int {
        if (i >= n) return if (prev == -1) 0 else nums[prev]
        var k = key(i, prev)
        var cached = memo[k]
        if (cached != null) return cached
        var res = 0
        if (prev == -1) {
            if (i + 1 >= n) res = nums[i]
            else if (i + 2 >= n) res = max2(nums[i], nums[i + 1])
            else {
                var a = nums[i]
                var b = nums[i + 1]
                var c = nums[i + 2]
                res = min3(max2(b, c) + dfs(i + 3, i), max2(a, c) + dfs(i + 3, i + 1), max2(a, b) + dfs(i + 3, i + 2))
            }
        } else {
            if (i + 1 >= n) res = max2(nums[prev], nums[i])
            else {
                var a = nums[prev]
                var b = nums[i]
                var c = nums[i + 1]
                res = min3(max2(b, c) + dfs(i + 2, prev), max2(a, c) + dfs(i + 2, i), max2(a, b) + dfs(i + 2, i + 1))
            }
        }
        memo[k] = res
        return res
    }

    fun minCost(nums: IntArray): Int {
        this.nums = nums
        n = nums.size
        memo.clear()
        return dfs(0, -1)
    }
}
