// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

class Solution {
    fun possibleBipartition(n: Int, dislikes: Array<IntArray>): Boolean {
        val graph = Array(n + 1) { mutableListOf<Int>() }
        for (e in dislikes) {
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        }
        val color = HashMap<Int, Int>()
        for (start in 1..n) {
            if (color.containsKey(start)) continue
            val queue = ArrayDeque<Int>()
            queue.add(start)
            color[start] = 0
            while (queue.isNotEmpty()) {
                val node = queue.removeFirst()
                for (nei in graph[node]) {
                    if (!color.containsKey(nei)) {
                        color[nei] = color[node]!! xor 1
                        queue.add(nei)
                    } else if (color[nei] == color[node]) {
                        return false
                    }
                }
            }
        }
        return true
    }
}
