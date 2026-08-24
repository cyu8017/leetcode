// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

class Solution {
    private lateinit var g: Array<ArrayList<IntArray>>
    private lateinit var nums: IntArray
    private var bestLen = 0
    private var bestNodes = 1
    private val last = HashMap<Int, Int>()

    fun longestSpecialPath(edges: Array<IntArray>, nums: IntArray): IntArray {
        this.nums = nums
        val n = nums.size
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(intArrayOf(e[1], e[2]))
            g[e[1]].add(intArrayOf(e[0], e[2]))
        }
        bestLen = 0
        bestNodes = 1
        last.clear()
        dfs(0, -1, 0, 0, ArrayList())
        return intArrayOf(bestLen, bestNodes)
    }

    private fun dfs(u: Int, p: Int, dist: Int, left: Int, path: MutableList<Int>) {
        var prevPos = -1
        val seen = last.containsKey(nums[u])
        if (seen) prevPos = last[nums[u]]!!
        last[nums[u]] = path.size
        var newLeft = left
        if (seen && prevPos >= left) newLeft = prevPos + 1
        path.add(dist)
        val length = dist - path[newLeft]
        val nodes = path.size - newLeft
        if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
            bestLen = length
            bestNodes = nodes
        }
        for (e in g[u]) {
            if (e[0] == p) continue
            dfs(e[0], u, dist + e[1], newLeft, path)
        }
        path.removeAt(path.size - 1)
        if (seen) last[nums[u]] = prevPos else last.remove(nums[u])
    }
}
