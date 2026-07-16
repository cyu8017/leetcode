// LeetCode 0285 - Inorder Successor in BST
// https://leetcode.com/problems/inorder-successor-in-bst/

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
    func inorderSuccessor(_ root: TreeNode?, _ p: TreeNode) -> TreeNode? {
        if let right = p.right {
            var current: TreeNode? = right
            while let left = current?.left {
                current = left
            }
            return current
        }
        var successor: TreeNode?
        var current = root
        while let node = current {
            if p.val < node.val {
                successor = node
                current = node.left
            } else {
                current = node.right
            }
        }
        return successor
    }
}
