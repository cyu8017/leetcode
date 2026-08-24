// LeetCode 0897 - Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

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
    private var cur: TreeNode?

    func increasingBST(_ root: TreeNode?) -> TreeNode? {
        let dummy = TreeNode(0)
        cur = dummy
        inorder(root)
        return dummy.right
    }

    private func inorder(_ node: TreeNode?) {
        guard let node = node else { return }
        inorder(node.left)
        node.left = nil
        cur?.right = node
        cur = node
        inorder(node.right)
    }
}
