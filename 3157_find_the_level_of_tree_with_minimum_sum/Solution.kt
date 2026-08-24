// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun minimumLevel(root: TreeNode?): Int {
        var q = ArrayDeque<TreeNode>()
        q.offer(root)
        var s = Long.MAX_VALUE
        var ans = 0
        var level = 1
        while (!q.isEmpty()) {
            var t = 0
            var m = q.size
            while (m-- > 0) {
                var node = q.poll()
                t += node.`val`
                if (node.left != null) q.offer(node.left)
                if (node.right != null) q.offer(node.right)
            }
            if (s > t) {
                s = t
                ans = level
            }
            level++
        }
        return ans
    }
}
