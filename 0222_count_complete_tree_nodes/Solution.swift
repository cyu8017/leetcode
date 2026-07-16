// LeetCode 0222 - Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

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
    func countNodes(_ root: TreeNode?) -> Int {
        guard let root = root else {
            return 0
        }
        let left = leftDepth(root)
        let right = rightDepth(root)
        if left == right {
            return (1 << left) - 1
        }
        return 1 + countNodes(root.left) + countNodes(root.right)
    }

    private func leftDepth(_ node: TreeNode?) -> Int {
        var depth = 0
        var current = node
        while let value = current {
            depth += 1
            current = value.left
        }
        return depth
    }

    private func rightDepth(_ node: TreeNode?) -> Int {
        var depth = 0
        var current = node
        while let value = current {
            depth += 1
            current = value.right
        }
        return depth
    }
}
