// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/

import java.util.ArrayDeque

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class BSTIterator(root: TreeNode?) {
    private val values = mutableListOf<Int>()
    private var index = -1

    init {
        val stack = ArrayDeque<TreeNode>()
        var cur = root
        while (stack.isNotEmpty() || cur != null) {
            while (cur != null) {
                stack.push(cur)
                cur = cur.left
            }
            cur = stack.pop()
            values.add(cur.`val`)
            cur = cur.right
        }
    }

    fun hasNext(): Boolean = index + 1 < values.size

    fun next(): Int = values[++index]

    fun hasPrev(): Boolean = index > 0

    fun prev(): Int = values[--index]
}
