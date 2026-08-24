// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution {
    private var target: Int = 0
    private var answer: MutableList<MutableList<Int>>? = null

    fun allPathsSourceTarget(graph: Array<IntArray>): MutableList<MutableList<Int>> {
        target = graph.size - 1
        answer = ArrayList()
        var path = ArrayList<Int>()
        path.add(0)
        dfs(graph, 0, path)
        return answer
    }

    private fun dfs(graph: Array<IntArray>, node: Int, path: MutableList<Int>) {
        if (node == target) {
            answer.add(ArrayList(path))
            return
        }
        for (nei in graph[node]) {
            path.add(nei)
            dfs(graph, nei, path)
            path.remove(path.size - 1)
        }
    }
}
