// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun createBinaryTree(descriptions: Array<IntArray>): TreeNode? {
        val nodes = HashMap<Int, TreeNode>()
        val child = HashSet<Int>()
        for (d in descriptions) {
            val p = d[0]
            val c = d[1]
            val isLeft = d[2]
            nodes.putIfAbsent(p, TreeNode(p))
            nodes.putIfAbsent(c, TreeNode(c))
            if (isLeft == 1) nodes[p]!!.left = nodes[c]
            else nodes[p]!!.right = nodes[c]
            child.add(c)
        }
        for ((k, v) in nodes) {
            if (k !in child) return v
        }
        return null
    }
}
