// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

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
    func longestUnivaluePath(_ root: TreeNode?) -> Int {
        var best = 0
        func dfs(_ node: TreeNode?) -> Int {
            guard let node else { return 0 }
            let left = dfs(node.left)
            let right = dfs(node.right)
            var leftPath = 0, rightPath = 0
            if node.left?.val == node.val { leftPath = left + 1 }
            if node.right?.val == node.val { rightPath = right + 1 }
            best = max(best, leftPath + rightPath)
            return max(leftPath, rightPath)
        }
        _ = dfs(root)
        return best
    }
}
