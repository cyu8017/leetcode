// LeetCode 1490 - Clone N-ary Tree
// https://leetcode.com/problems/clone-n-ary-tree/

class Node(var `val`: Int) {
    var children: MutableList<Node?> = mutableListOf()
}

class Solution {
    fun cloneTree(root: Node?): Node? {
        if (root == null) return null
        val copy = Node(root.`val`)
        copy.children = root.children.map { cloneTree(it) }.toMutableList()
        return copy
    }
}
