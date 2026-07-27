// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

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
    func lowestCommonAncestor(_ root: TreeNode?, _ nodes: [TreeNode?]) -> TreeNode? {
        var targets = Set(nodes.compactMap { $0 }.map { ObjectIdentifier($0) })
        var vals = Set(nodes.compactMap { $0?.val })
        func match(_ node: TreeNode?) -> Bool {
            guard let node = node else { return false }
            return targets.contains(ObjectIdentifier(node)) || vals.contains(node.val)
        }
        func dfs(_ node: TreeNode?) -> TreeNode? {
            guard let node = node else { return nil }
            let l = dfs(node.left)
            let r = dfs(node.right)
            if match(node) || (l != nil && r != nil) { return node }
            return l ?? r
        }
        return dfs(root)
    }
}
