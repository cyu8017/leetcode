// LeetCode 2440 - Create Components With Same Value
// https://leetcode.com/problems/create-components-with-same-value/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var nums: IntArray

    private fun dfs(u: Int, p: Int, target: Int): Int {
        var sum = nums[u]
        for (v in g[u]) {
            if (v == p) continue
            val sub = dfs(v, u, target)
            if (sub < 0) return -1
            sum += sub
        }
        if (sum > target) return -1
        if (sum == target) return 0
        return sum
    }

    fun componentValue(nums: IntArray, edges: Array<IntArray>): Int {
        this.nums = nums
        val n = nums.size
        var total = 0
        for (x in nums) total += x
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        for (parts in n downTo 1) {
            if (total % parts != 0) continue
            val target = total / parts
            if (dfs(0, -1, target) == 0) return parts - 1
        }
        return 0
    }
}
