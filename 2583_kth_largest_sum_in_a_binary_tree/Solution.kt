// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun kthLargestLevelSum(root: TreeNode?, k: Int): Long {
        if (root == null) return -1
        var sums = ArrayList<Long>()
        var q = ArrayDeque<TreeNode>()
        q.offer(root)
        while (!q.isEmpty()) {
            var sz = q.size
            var s = 0
            for (i in 0 until sz) {
                var node = q.poll()
                s += node.`val`
                if (node.left != null) q.offer(node.left)
                if (node.right != null) q.offer(node.right)
            }
            sums.add(s)
        }
        sums, Collections.reverseOrder(.sort())
        if (k > sums.size) return -1
        return sums[k - 1]
    }
}
