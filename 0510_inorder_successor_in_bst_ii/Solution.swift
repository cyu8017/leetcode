// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

class Node {
    var val: Int
    var left: Node?
    var right: Node?
    weak var parent: Node?
    init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
        self.parent = nil
    }
}

class Solution {
    func inorderSuccessor(_ node: Node) -> Node? {
        if let right = node.right {
            var current = right
            while let left = current.left {
                current = left
            }
            return current
        }
        var current: Node? = node
        while let parent = current?.parent, current === parent.right {
            current = parent
        }
        return current?.parent
    }
}
