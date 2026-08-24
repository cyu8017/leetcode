// LeetCode 0783 - Minimum Distance Between BST Nodes
// https://leetcode.com/problems/minimum-distance-between-bst-nodes/

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
    private var hasPrev = false
    private var prev = 0
    private var best = Int.max

    func minDiffInBST(_ root: TreeNode?) -> Int {
        hasPrev = false
        best = Int.max
        inorder(root)
        return best
    }

    private func inorder(_ node: TreeNode?) {
        guard let node = node else { return }
        inorder(node.left)
        if hasPrev { best = min(best, node.val - prev) }
        prev = node.val
        hasPrev = true
        inorder(node.right)
    }
}
