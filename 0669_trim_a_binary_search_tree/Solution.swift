// LeetCode 0669 - Trim a Binary Search Tree
// https://leetcode.com/problems/trim-a-binary-search-tree/

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
    func trimBST(_ root: TreeNode?, _ low: Int, _ high: Int) -> TreeNode? {
        guard let root else { return nil }
        if root.val < low { return trimBST(root.right, low, high) }
        if root.val > high { return trimBST(root.left, low, high) }
        root.left = trimBST(root.left, low, high)
        root.right = trimBST(root.right, low, high)
        return root
    }
}
