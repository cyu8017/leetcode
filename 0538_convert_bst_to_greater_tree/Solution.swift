// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

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
    func convertBST(_ root: TreeNode?) {
        var running = 0

        func reverseInorder(_ node: TreeNode?) {
            guard let node else { return }
            reverseInorder(node.right)
            running += node.val
            node.val = running
            reverseInorder(node.left)
        }

        reverseInorder(root)
    }
}
