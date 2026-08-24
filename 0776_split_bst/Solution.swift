// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

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
    func splitBST(_ root: TreeNode?, _ target: Int) -> [TreeNode?] {
        guard let root else { return [nil, nil] }
        if root.val <= target {
            let parts = splitBST(root.right, target)
            root.right = parts[0]
            return [root, parts[1]]
        }
        let leftParts = splitBST(root.left, target)
        root.left = leftParts[1]
        return [leftParts[0], root]
    }
}
