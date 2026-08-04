// LeetCode 1379 - Find a Corresponding Node of a Binary Tree in a Clone of That Tree
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun getTargetCopy(original: TreeNode?, cloned: TreeNode?, target: TreeNode?): TreeNode? {
        if (original == null || cloned == null || target == null) return null
        val stack = ArrayDeque<Pair<TreeNode, TreeNode>>()
        stack.add(original to cloned)
        while (stack.isNotEmpty()) {
            val (a, b) = stack.removeLast()
            if (a === target || a.`val` == target.`val`) return b
            if (a.left != null) stack.add(a.left!! to b.left!!)
            if (a.right != null) stack.add(a.right!! to b.right!!)
        }
        return null
    }
}
