// LeetCode 3902 - Zigzag Level Sum Of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun zigzagLevelSum(root: TreeNode?): LongArray {
        var ans = ArrayList<Long>()
        var q = ArrayList<TreeNode>()
        q.add(root)
        var left = true
        while (!q.isEmpty()) {
            var nq = ArrayList<TreeNode>()
            for (node in q) {
                if (node.left != null) nq.add(node.left)
                if (node.right != null) nq.add(node.right)
            }
            var m = q.size
            var s = 0
            for (i in 0 until m) {
                var node = if (left) q[i] else q[m - i - 1]
                var child = if (left) node.left else node.right
                if (child == null) break
                s += node.`val`
            }
            ans.add(s)
            left = !left
            q = nq
        }
        var out = LongArray(ans.size)
        for (i in 0 until ans.size) { out[i] = ans[i] }
        return out
    }
}
