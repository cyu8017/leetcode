// LeetCode 0444 - Sequence Reconstruction
// https://leetcode.com/problems/sequence-reconstruction/

class Solution {
    fun sequenceReconstruction(nums: IntArray, sequences: List<List<Int>>): Boolean {
        val indegree = nums.associateWith { 0 }.toMutableMap()
        val graph = nums.associateWith { mutableSetOf<Int>() }.toMutableMap()
        val seenEdges = HashSet<Pair<Int, Int>>()

        for (sequence in sequences) {
            for (index in 0 until sequence.size - 1) {
                val left = sequence[index]
                val right = sequence[index + 1]
                if (!seenEdges.add(left to right)) {
                    continue
                }
                graph.getValue(left).add(right)
                indegree[right] = indegree.getValue(right) + 1
            }
        }

        val queue = ArrayDeque(nums.filter { indegree.getValue(it) == 0 })
        val order = mutableListOf<Int>()
        while (queue.isNotEmpty()) {
            if (queue.size > 1) {
                return false
            }
            val node = queue.removeFirst()
            order.add(node)
            for (neighbor in graph.getValue(node)) {
                indegree[neighbor] = indegree.getValue(neighbor) - 1
                if (indegree.getValue(neighbor) == 0) {
                    queue.add(neighbor)
                }
            }
        }

        return order == nums.toList()
    }
}
