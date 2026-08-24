// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

class Solution {
    private lateinit var graph: Array<ArrayList<Int>>
    private lateinit var count: IntArray
    private lateinit var ans: IntArray
    private var n = 0

    fun sumOfDistancesInTree(n: Int, edges: Array<IntArray>): IntArray {
        this.n = n
        graph = Array(n) { ArrayList() }
        for (e in edges) {
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        }
        count = IntArray(n) { 1 }
        ans = IntArray(n)
        post(0, -1)
        reroot(0, -1)
        return ans
    }

    private fun post(node: Int, parent: Int) {
        for (child in graph[node]) {
            if (child == parent) continue
            post(child, node)
            count[node] += count[child]
            ans[node] += ans[child] + count[child]
        }
    }

    private fun reroot(node: Int, parent: Int) {
        for (child in graph[node]) {
            if (child == parent) continue
            ans[child] = ans[node] - count[child] + (n - count[child])
            reroot(child, node)
        }
    }
}
