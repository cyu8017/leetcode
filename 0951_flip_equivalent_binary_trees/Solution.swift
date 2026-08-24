// LeetCode 0951 - Flip Equivalent Binary Trees
// https://leetcode.com/problems/flip-equivalent-binary-trees/

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
    func flipEquiv(_ root1: TreeNode?, _ root2: TreeNode?) -> Bool {
        if root1 == nil && root2 == nil { return true }
        guard let a = root1, let b = root2, a.val == b.val else { return false }
        return (flipEquiv(a.left, b.left) && flipEquiv(a.right, b.right))
            || (flipEquiv(a.left, b.right) && flipEquiv(a.right, b.left))
    }
}
