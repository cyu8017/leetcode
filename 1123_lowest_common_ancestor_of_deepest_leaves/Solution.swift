// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

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
    func lcaDeepestLeaves(_ root: TreeNode?) -> TreeNode? {
        func dfs(_ node: TreeNode?) -> (Int, TreeNode?) {
            guard let node = node else { return (0, nil) }
            let left = dfs(node.left)
            let right = dfs(node.right)
            if left.0 > right.0 { return (left.0 + 1, left.1) }
            if right.0 > left.0 { return (right.0 + 1, right.1) }
            return (left.0 + 1, node)
        }
        return dfs(root).1
    }
}
