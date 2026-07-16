// LeetCode 0156 - Binary Tree Upside Down
// https://leetcode.com/problems/binary-tree-upside-down/

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?

    init(_ val: Int = 0, _ left: TreeNode? = nil, _ right: TreeNode? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func upsideDownBinaryTree(_ root: TreeNode?) -> TreeNode? {
        var previous: TreeNode?
        var previousRight: TreeNode?
        var current = root
        while let node = current {
            let next = node.left
            node.left = previousRight
            previousRight = node.right
            node.right = previous
            previous = node
            current = next
        }
        return previous
    }
}