// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

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
    func maximumAverageSubtree(_ root: TreeNode?) -> Double {
        var best = 0.0
        func dfs(_ node: TreeNode?) -> (Int, Int) {
            guard let node = node else { return (0, 0) }
            let left = dfs(node.left)
            let right = dfs(node.right)
            let totalSum = left.0 + right.0 + node.val
            let totalCount = left.1 + right.1 + 1
            best = max(best, Double(totalSum) / Double(totalCount))
            return (totalSum, totalCount)
        }
        _ = dfs(root)
        return best
    }
}
