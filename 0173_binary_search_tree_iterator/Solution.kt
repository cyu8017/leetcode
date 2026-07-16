import java.util.ArrayDeque

class TreeNode(var `val`: Int = 0, var left: TreeNode? = null, var right: TreeNode? = null)

class BSTIterator(root: TreeNode?) {
    private val stack = ArrayDeque<TreeNode>()

    init {
        pushLeft(root)
    }

    fun next(): Int {
        val node = stack.removeLast()
        pushLeft(node.right)
        return node.`val`
    }

    fun hasNext(): Boolean = stack.isNotEmpty()

    private fun pushLeft(start: TreeNode?) {
        var node = start
        while (node != null) {
            stack.addLast(node)
            node = node.left
        }
    }
}
