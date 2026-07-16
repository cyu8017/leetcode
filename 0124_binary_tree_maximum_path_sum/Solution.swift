// LeetCode 0124 - Binary Tree Maximum Path Sum
// https://leetcode.com/problems/binary-tree-maximum-path-sum/

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init() { self.val = 0; self.left = nil; self.right = nil }
    init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func maxPathSum(_ root: TreeNode?) -> Int {
        var best = Int.min

        func gain(_ node: TreeNode?) -> Int {
            guard let node = node else { return 0 }
            let left = max(gain(node.left), 0)
            let right = max(gain(node.right), 0)
            best = max(best, node.val + left + right)
            return node.val + max(left, right)
        }

        _ = gain(root)
        return best
    }
}