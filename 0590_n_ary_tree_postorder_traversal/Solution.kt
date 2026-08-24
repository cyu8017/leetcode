// LeetCode 0590 - N-ary Tree Postorder Traversal
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

class Node(var `val`: Int = 0) {
    var children: List<Node>? = null
}

class Solution {
    fun postorder(root: Node?): List<Int> {
        val result = ArrayList<Int>()
        dfs(root, result)
        return result
    }

    private fun dfs(node: Node?, result: MutableList<Int>) {
        if (node == null) return
        node.children?.forEach { dfs(it, result) }
        result.add(node.`val`)
    }
}
