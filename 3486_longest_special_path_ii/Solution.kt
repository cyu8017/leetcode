// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

class Solution {
    private lateinit var g: Array<ArrayList<IntArray>>
    private lateinit var nums: IntArray
    private var bestLen = 0
    private var bestNodes = 1

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
        dfs(0, -1, 0, ArrayList(), ArrayList())
        return intArrayOf(bestLen, bestNodes)
    }

    private fun dfs(u: Int, p: Int, dist: Int, pathVals: MutableList<Int>, pathDist: MutableList<Int>) {
        pathVals.add(nums[u])
        pathDist.add(dist)
        val freq = HashMap<Int, Int>()
        var dups = 0
        var left = 0
        for (right in pathVals.indices) {
            val v = pathVals[right]
            freq[v] = freq.getOrDefault(v, 0) + 1
            if (freq[v] == 2) dups++
            while (dups > 1) {
                val lv = pathVals[left]
                if (freq[lv] == 2) dups--
                freq[lv] = freq[lv]!! - 1
                left++
            }
        }
        val length = dist - pathDist[left]
        val nodes = pathVals.size - left
        if (length > bestLen || (length == bestLen && nodes < bestNodes)) {
            bestLen = length
            bestNodes = nodes
        }
        for (e in g[u]) {
            if (e[0] == p) continue
            dfs(e[0], u, dist + e[1], pathVals, pathDist)
        }
        pathVals.removeAt(pathVals.size - 1)
        pathDist.removeAt(pathDist.size - 1)
    }
}
