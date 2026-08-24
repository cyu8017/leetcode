// LeetCode 0589 - N-ary Tree Preorder Traversal
// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Node(var `val`: Int = 0) {
    var children: List<Node>? = null
}

class Solution {
    fun preorder(root: Node?): List<Int> {
        val result = ArrayList<Int>()
        dfs(root, result)
        return result
    }

    private fun dfs(node: Node?, result: MutableList<Int>) {
        if (node == null) return
        result.add(node.`val`)
        node.children?.forEach { dfs(it, result) }
    }
}
