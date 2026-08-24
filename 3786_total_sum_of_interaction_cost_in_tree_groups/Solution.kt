// LeetCode 3786 - Total Sum Of Interaction Cost In Tree Groups
// https://leetcode.com/problems/total_sum_of_interaction_cost_in_tree_groups/

class Solution {
    fun interactionCost(n: Int, edges: Array<IntArray>, group: IntArray): Long {
        val g = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        val total = IntArray(21)
        for (x in group) total[x]++
        val parent = IntArray(n) { -2 }
        parent[0] = -1
        val order = ArrayList<Int>()
        order.add(0)
        var i = 0
        while (i < order.size) {
            val u = order[i++]
            for (v in g[u]) {
                if (parent[v] == -2) {
                    parent[v] = u
                    order.add(v)
                }
            }
        }
        val count = Array(n) { IntArray(21) }
        var ans = 0L
        for (idx in n - 1 downTo 0) {
            val u = order[idx]
            count[u][group[u]]++
            for (v in g[u]) {
                if (parent[v] != u) continue
                for (c in 1..20) {
                    val x = count[v][c]
                    ans += x.toLong() * (total[c] - x)
                    count[u][c] += x
                }
            }
        }
        return ans
    }
}
