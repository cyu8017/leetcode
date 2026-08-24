// LeetCode 0606 - Construct String from Binary Tree
// https://leetcode.com/problems/construct-string-from-binary-tree/

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
    func tree2str(_ root: TreeNode?) -> String {
        guard let root else { return "" }
        var result = String(root.val)
        if root.left != nil || root.right != nil {
            result += "(" + tree2str(root.left) + ")"
        }
        if root.right != nil {
            result += "(" + tree2str(root.right) + ")"
        }
        return result
    }
}
