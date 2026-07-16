// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

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
    private var first: TreeNode?
    private var last: TreeNode?

    func treeToDoublyList(_ root: TreeNode?) -> TreeNode? {
        guard let root else {
            return nil
        }

        first = nil
        last = nil
        inorder(root)
        if let first, let last {
            first.left = last
            last.right = first
        }
        return first
    }

    private func inorder(_ node: TreeNode?) {
        guard let node else {
            return
        }
        inorder(node.left)
        if let last {
            last.right = node
            node.left = last
        } else {
            first = node
        }
        last = node
        inorder(node.right)
    }
}
