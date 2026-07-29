// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

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
    func maxAncestorDiff(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        func dfs(_ node: TreeNode?, _ lo: Int, _ hi: Int) -> Int {
            guard let node = node else { return hi - lo }
            let lo = min(lo, node.val)
            let hi = max(hi, node.val)
            return max(dfs(node.left, lo, hi), dfs(node.right, lo, hi))
        }
        return dfs(root, root.val, root.val)
    }
}
