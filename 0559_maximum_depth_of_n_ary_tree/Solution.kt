// LeetCode 0559 - Maximum Depth of N-ary Tree
// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Node(var `val`: Int = 0) {
    var children: List<Node>? = null
}

class Solution {
    fun maxDepth(root: Node?): Int {
        if (root == null) return 0
        val children = root.children
        if (children.isNullOrEmpty()) return 1
        var best = 0
        for (child in children) best = maxOf(best, maxDepth(child))
        return best + 1
    }
}
