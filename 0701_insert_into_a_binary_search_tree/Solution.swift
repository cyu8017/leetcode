// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

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
    func insertIntoBST(_ root: TreeNode?, _ val: Int) -> TreeNode? {
        guard let root else { return TreeNode(val) }
        if val < root.val { root.left = insertIntoBST(root.left, val) }
        else { root.right = insertIntoBST(root.right, val) }
        return root
    }
}
