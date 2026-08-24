// LeetCode 0572 - Subtree of Another Tree
// https://leetcode.com/problems/subtree-of-another-tree/

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
    func isSubtree(_ root: TreeNode?, _ subRoot: TreeNode?) -> Bool {
        guard let root else { return false }
        return same(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
    }

    private func same(_ a: TreeNode?, _ b: TreeNode?) -> Bool {
        if a == nil || b == nil { return a == nil && b == nil }
        return a!.val == b!.val && same(a!.left, b!.left) && same(a!.right, b!.right)
    }
}
