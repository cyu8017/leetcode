// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class FindElements(root: TreeNode?) {
    private val values = mutableSetOf<Int>()

    init {
        recover(root, 0)
    }

    private fun recover(node: TreeNode?, value: Int) {
        if (node == null) return
        node.`val` = value
        values.add(value)
        recover(node.left, 2 * value + 1)
        recover(node.right, 2 * value + 2)
    }

    fun find(target: Int): Boolean = target in values
}
