// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

class Solution {
    fun maxStarSum(vals: IntArray, edges: Array<IntArray>, k: Int): Int {
        val n = vals.size
        val g = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        var ans = vals[0]
        for (i in 0 until n) {
            val neigh = ArrayList<Int>()
            for (v in g[i]) if (vals[v] > 0) neigh.add(vals[v])
            neigh.sortDescending()
            var sum = vals[i]
            var j = 0
            while (j < neigh.size && j < k) {
                sum += neigh[j]
                j++
            }
            if (sum > ans) ans = sum
        }
        return ans
    }
}
