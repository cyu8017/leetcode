class TreeNode(var `val`: Int = 0, var left: TreeNode? = null, var right: TreeNode? = null)

class Solution {
    fun rightSideView(root: TreeNode?): List<Int> {
        if (root == null) return emptyList()
        val result = mutableListOf<Int>()
        val queue = java.util.ArrayDeque<TreeNode>()
        queue.add(root)
        while (queue.isNotEmpty()) {
            val size = queue.size
            repeat(size) { index ->
                val node = queue.removeFirst()
                if (index == size - 1) result.add(node.`val`)
                node.left?.let(queue::addLast)
                node.right?.let(queue::addLast)
            }
        }
        return result
    }
}
