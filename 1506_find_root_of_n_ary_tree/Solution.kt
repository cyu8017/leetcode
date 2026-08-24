// LeetCode 1506 - Find Root of N-Ary Tree
// https://leetcode.com/problems/find-root-of-n-ary-tree/

class Node(var `val`: Int) {
    var children: MutableList<Node> = mutableListOf()
}

class Solution {
    fun findRoot(tree: List<Node>): Node? {
        var value = 0
        val nodes = HashMap<Int, Node>()
        for (node in tree) {
            nodes[node.`val`] = node
            value = value xor node.`val`
            for (child in node.children) {
                value = value xor child.`val`
            }
        }
        return nodes[value]
    }
}
