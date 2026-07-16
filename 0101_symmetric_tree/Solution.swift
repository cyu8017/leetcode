// LeetCode 0101 - Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

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
    func isSymmetric(_ root: TreeNode?) -> Bool {
        guard let root = root else {
            return true
        }
        return mirrors(root.left, root.right)
    }

    private func mirrors(_ left: TreeNode?, _ right: TreeNode?) -> Bool {
        if left == nil && right == nil {
            return true
        }
        guard let left = left, let right = right, left.val == right.val else {
            return false
        }
        return mirrors(left.left, right.right) && mirrors(left.right, right.left)
    }
}
