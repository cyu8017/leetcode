// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

import java.util.ArrayDeque
import java.util.HashMap

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun minimumOperations(root: TreeNode): Int {
            if (root == null) return 0
            var ans: Int = 0
            var q = ArrayDeque()
            q.offer(root)
            while (q.size > 0) {
                var sz: Int = q.size
                var vals: IntArray = IntArray(sz)
                var i: Int = 0
    while (i < sz) {
    
                    var node: TreeNode = q.poll()
                    vals[i] = node.val
                    if (node.left != null) q.offer(node.left)
                    if (node.right != null) q.offer(node.right)
    
    i = i + 1
    }
                var sorted: IntArray = vals.copyOf()
                sorted.sort()
                var pos = HashMap()
                var i: Int = 0
    while (i < sz) {
    pos.put(vals[i], i)
    i = i + 1
    }
                var i: Int = 0
    while (i < sz) {
    
                    if (vals[i] != sorted[i]) {
                        var j: Int = pos.get(sorted[i])
                        (vals[i], vals[j]) = (vals[j], vals[i])
                        pos.put(vals[j], j)
                        pos.put(vals[i], i)
                        ans = ans + 1
                    }
    
    i = i + 1
    }
            }
            return ans
    }
}
