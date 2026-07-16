// LeetCode 0235 - Lowest Common Ancestor of a Binary Search Tree
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?

    init(_ val: Int = 0, _ left: TreeNode? = nil, _ right: TreeNode? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func lowestCommonAncestor(_ root: TreeNode?, _ p: TreeNode, _ q: TreeNode) -> TreeNode? {
        var current = root
        while let node = current {
            if p.val < node.val && q.val < node.val {
                current = node.left
            } else if p.val > node.val && q.val > node.val {
                current = node.right
            } else {
                return node
            }
        }
        return current
    }
}
