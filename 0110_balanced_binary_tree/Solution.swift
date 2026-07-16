// LeetCode 0110 - Balanced Binary Tree
// https://leetcode.com/problems/balanced-binary-tree/

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
    func isBalanced(_ root: TreeNode?) -> Bool {
        return height(root) != -1
    }

    private func height(_ node: TreeNode?) -> Int {
        guard let node = node else {
            return 0
        }
        let left = height(node.left)
        if left == -1 {
            return -1
        }
        let right = height(node.right)
        if right == -1 {
            return -1
        }
        if abs(left - right) > 1 {
            return -1
        }
        return 1 + max(left, right)
    }
}
