// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun findMode(root: TreeNode?): IntArray {
        val counts = mutableMapOf<Int, Int>()
        var best = 0
        inorder(root, counts) { count -> best = maxOf(best, count) }
        return counts.filter { it.value == best }.keys.toIntArray()
    }

    private fun inorder(
        node: TreeNode?,
        counts: MutableMap<Int, Int>,
        onCount: (Int) -> Unit,
    ) {
        if (node == null) {
            return
        }
        inorder(node.left, counts, onCount)
        val count = counts.getOrDefault(node.`val`, 0) + 1
        counts[node.`val`] = count
        onCount(count)
        inorder(node.right, counts, onCount)
    }
}
