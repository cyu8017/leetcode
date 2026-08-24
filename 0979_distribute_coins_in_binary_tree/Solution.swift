// LeetCode 0979 - Distribute Coins in Binary Tree
// https://leetcode.com/problems/distribute-coins-in-binary-tree/

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
    private var ans = 0

    func distributeCoins(_ root: TreeNode?) -> Int {
        ans = 0
        _ = dfs(root)
        return ans
    }

    private func dfs(_ node: TreeNode?) -> Int {
        guard let node = node else { return 0 }
        let left = dfs(node.left)
        let right = dfs(node.right)
        ans += abs(left) + abs(right)
        return node.val + left + right - 1
    }
}
