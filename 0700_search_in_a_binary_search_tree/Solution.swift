// LeetCode 0700 - Search in a Binary Search Tree
// https://leetcode.com/problems/search-in-a-binary-search-tree/

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
    func searchBST(_ root: TreeNode?, _ val: Int) -> TreeNode? {
        guard let root else { return nil }
        if root.val == val { return root }
        return val < root.val ? searchBST(root.left, val) : searchBST(root.right, val)
    }
}
