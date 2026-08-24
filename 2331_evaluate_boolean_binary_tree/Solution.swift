// LeetCode 2331 - Evaluate Boolean Binary Tree
// https://leetcode.com/problems/evaluate-boolean-binary-tree/

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
    func evaluateTree(_ root: TreeNode?) -> Bool {
        guard let root = root else { return false }
        if root.left == nil && root.right == nil { return root.val == 1 }
        let l = evaluateTree(root.left)
        let r = evaluateTree(root.right)
        return root.val == 2 ? (l || r) : (l && r)
    }
}
