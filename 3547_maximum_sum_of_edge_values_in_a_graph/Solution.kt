// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

class Solution {
    fun calc(left: Int, right: Int, isCycle: Boolean): Long {
        var w0 = right
        var w1 = right
        var score = 0L
        for (value in right - 1 downTo left) {
            score += 1L * w0 * value
            w0 = w1
            w1 = value
        }
        if (isCycle) score += 1L * w0 * w1
        return score
    }

    fun maxScore(n: Int, edges: Array<IntArray>): Long {
        val graph = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        }
        val seen = BooleanArray(n)
        val cycleSizes = ArrayList<Int>()
        val pathSizes = ArrayList<Int>()
        for (i in 0 until n) {
            if (seen[i]) continue
            val comp = getComp(i, graph, seen)
            var allDeg2 = true
            for (u in comp) if (graph[u].size != 2) { allDeg2 = false; break }
            if (allDeg2) cycleSizes.add(comp.size)
            else if (comp.size > 1) pathSizes.add(comp.size)
        }
        var ans = 0L
        var curN = n
        for (cs in cycleSizes) {
            ans += calc(curN - cs + 1, curN, true)
            curN -= cs
        }
        pathSizes.sortDescending()
        for (ps in pathSizes) {
            ans += calc(curN - ps + 1, curN, false)
            curN -= ps
        }
        return ans
    }

    fun getComp(start: Int, graph: Array<ArrayList<Int>>, seen: BooleanArray): ArrayList<Int> {
        val comp = ArrayList<Int>()
        comp.add(start)
        seen[start] = true
        var i = 0
        while (i < comp.size) {
            for (v in graph[comp[i]]) {
                if (!seen[v]) {
                    seen[v] = true
                    comp.add(v)
                }
            }
            i++
        }
        return comp
    }
}
