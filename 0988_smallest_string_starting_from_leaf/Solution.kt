// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    private var best: String = "~"

    fun smallestFromLeaf(root: TreeNode?): String {
best = "~"
dfs(root, "")
return best
}

    private fun dfs(node: TreeNode?, path: String) {
if (node == null) {
return
}
path = (char) ('a' + node.`val`) + path
if (node.left == null && node.right == null) {
if (path.compareTo(best) < 0) {
best = path
}
return
}
dfs(node.left, path)
dfs(node.right, path)
}
}
