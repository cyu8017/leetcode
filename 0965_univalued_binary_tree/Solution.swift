// LeetCode 0965 - Univalued Binary Tree
// https://leetcode.com/problems/univalued-binary-tree/

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
    func isUnivalTree(_ root: TreeNode?) -> Bool {
        guard let root = root else { return true }
        func dfs(_ node: TreeNode?, _ v: Int) -> Bool {
            guard let node = node else { return true }
            if node.val != v { return false }
            return dfs(node.left, v) && dfs(node.right, v)
        }
        return dfs(root, root.val)
    }
}
