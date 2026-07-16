// LeetCode 0138 - Copy List with Random Pointer
// https://leetcode.com/problems/copy-list-with-random-pointer/

class Solution {
    fun copyRandomList(head: Node?): Node? {
        val clones = HashMap<Node, Node>()
        fun copy(node: Node?): Node? {
            if (node == null) return null
            clones[node]?.let { return it }
            val clone = Node(node.`val`)
            clones[node] = clone
            clone.next = copy(node.next)
            clone.random = copy(node.random)
            return clone
        }
        return copy(head)
    }
}
