// LeetCode 1305 - All Elements in Two Binary Search Trees
// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun getAllElements(root1: TreeNode?, root2: TreeNode?): List<Int> {
        fun inorder(root: TreeNode?): List<Int> {
            if (root == null) return emptyList()
            return inorder(root.left) + root.`val` + inorder(root.right)
        }
        val a = inorder(root1)
        val b = inorder(root2)
        val answer = mutableListOf<Int>()
        var i = 0
        var j = 0
        while (i < a.size || j < b.size) {
            if (j == b.size || (i < a.size && a[i] <= b[j])) {
                answer.add(a[i++])
            } else {
                answer.add(b[j++])
            }
        }
        return answer
    }
}
