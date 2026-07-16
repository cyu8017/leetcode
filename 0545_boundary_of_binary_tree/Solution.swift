// LeetCode 0545 - Boundary of Binary Tree
// https://leetcode.com/problems/boundary-of-binary-tree/

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
    func boundaryOfBinaryTree(_ root: TreeNode?) -> [Int] {
        guard let root else { return [] }

        func isLeaf(_ node: TreeNode?) -> Bool {
            guard let node else { return false }
            return node.left == nil && node.right == nil
        }

        func leftBoundary(_ node: TreeNode?) -> [Int] {
            guard let node, !isLeaf(node) else { return [] }
            if let left = node.left {
                return [node.val] + leftBoundary(left)
            }
            return [node.val] + leftBoundary(node.right)
        }

        func rightBoundary(_ node: TreeNode?) -> [Int] {
            guard let node, !isLeaf(node) else { return [] }
            if let right = node.right {
                return rightBoundary(right) + [node.val]
            }
            return rightBoundary(node.left) + [node.val]
        }

        func leaves(_ node: TreeNode?) -> [Int] {
            guard let node else { return [] }
            if isLeaf(node) {
                return [node.val]
            }
            return leaves(node.left) + leaves(node.right)
        }

        if isLeaf(root) {
            return [root.val]
        }

        return [root.val] + leftBoundary(root.left) + leaves(root) + rightBoundary(root.right)
    }
}
