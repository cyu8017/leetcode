// LeetCode 0543 - Diameter of Binary Tree
// https://leetcode.com/problems/diameter-of-binary-tree/

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
    func diameterOfBinaryTree(_ root: TreeNode?) -> Int {
        var best = 0

        func depth(_ node: TreeNode?) -> Int {
            guard let node else { return 0 }
            let left = depth(node.left)
            let right = depth(node.right)
            best = max(best, left + right)
            return 1 + max(left, right)
        }

        _ = depth(root)
        return best
    }
}
