// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

class Solution {
    private lateinit var g: HashMap<Int, MutableList<Int>>
    private lateinit var path: MutableList<Int>

    private fun dfs(u: Int) {
        val nbrs = g.getOrPut(u) { mutableListOf() }
        while (nbrs.isNotEmpty()) {
            val v = nbrs.removeAt(nbrs.size - 1)
            dfs(v)
        }
        path.add(u)
    }

    fun validArrangement(pairs: Array<IntArray>): Array<IntArray> {
        g = HashMap()
        val indeg = HashMap<Int, Int>()
        val outdeg = HashMap<Int, Int>()
        for (p in pairs) {
            val u = p[0]
            val v = p[1]
            g.getOrPut(u) { mutableListOf() }.add(v)
            outdeg[u] = outdeg.getOrDefault(u, 0) + 1
            indeg[v] = indeg.getOrDefault(v, 0) + 1
        }
        var start = pairs[0][0]
        for ((k, v) in outdeg) {
            if (v - indeg.getOrDefault(k, 0) == 1) {
                start = k
                break
            }
        }
        path = mutableListOf()
        dfs(start)
        path.reverse()
        val ans = Array(path.size - 1) { IntArray(2) }
        for (i in 0 until path.size - 1) {
            ans[i][0] = path[i]
            ans[i][1] = path[i + 1]
        }
        return ans
    }
}
