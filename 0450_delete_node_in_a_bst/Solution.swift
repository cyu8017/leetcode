// LeetCode 0450 - Delete Node in a BST
// https://leetcode.com/problems/delete-node-in-a-bst/

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
    func deleteNode(_ root: TreeNode?, _ key: Int) -> TreeNode? {
        guard let root else {
            return nil
        }
        if key < root.val {
            root.left = deleteNode(root.left, key)
        } else if key > root.val {
            root.right = deleteNode(root.right, key)
        } else {
            if root.left == nil {
                return root.right
            }
            if root.right == nil {
                return root.left
            }
            var successor = root.right!
            while let left = successor.left {
                successor = left
            }
            root.val = successor.val
            root.right = deleteNode(root.right, successor.val)
        }
        return root
    }
}
