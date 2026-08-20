// LeetCode 1448 - Count Good Nodes in Binary Tree
// https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init() { self.val = 0; self.left = nil; self.right = nil }
    init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val; self.left = left; self.right = right
    }
}

class Solution {
    func goodNodes(_ root: TreeNode?) -> Int {
        func visit(_ node: TreeNode?, _ maximum: Int) -> Int {
            guard let node = node else { return 0 }
            let good = node.val >= maximum ? 1 : 0
            let m = max(maximum, node.val)
            return good + visit(node.left, m) + visit(node.right, m)
        }
        return visit(root, Int.min)
    }
}
