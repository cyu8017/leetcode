// LeetCode 0133 - Clone Graph
// https://leetcode.com/problems/clone-graph/

class Solution {
    fun cloneGraph(node: Node?): Node? {
        val clones = HashMap<Node, Node>()
        fun clone(current: Node?): Node? {
            if (current == null) return null
            clones[current]?.let { return it }
            val copy = Node(current.`val`)
            clones[current] = copy
            for (neighbor in current.neighbors) copy.neighbors.add(clone(neighbor))
            return copy
        }
        return clone(node)
    }
}
