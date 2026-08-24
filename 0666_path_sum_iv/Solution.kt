// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/


class Solution {
    fun pathSum(nums: IntArray): Int {
        val map = HashMap<Int, Int>()
        for (num in nums) {
            val pos = num / 10
            map[pos] = num % 10
        }
        var total = 0
        fun dfs(pos: Int, sum: Int) {
            if (pos !in map) return
            val cur = sum + map[pos]!!
            val depth = pos / 10
            val offset = pos % 10
            val left = (depth + 1) * 10 + (offset * 2 - 1)
            val right = (depth + 1) * 10 + (offset * 2)
            if (left !in map && right !in map) {
                total += cur
                return
            }
            dfs(left, cur)
            dfs(right, cur)
        }
        dfs(11, 0)
        return total
    }
}
