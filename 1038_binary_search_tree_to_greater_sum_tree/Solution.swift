// LeetCode 1038 - Binary Search Tree to Greater Sum Tree
// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

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
    func bstToGst(_ root: TreeNode?) -> TreeNode? {
        var total = 0
        func reverseInorder(_ node: TreeNode?) {
            guard let node = node else { return }
            reverseInorder(node.right)
            total += node.val
            node.val = total
            reverseInorder(node.left)
        }
        reverseInorder(root)
        return root
    }
}
