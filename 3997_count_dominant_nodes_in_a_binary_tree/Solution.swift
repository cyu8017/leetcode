// LeetCode 3997 - Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/


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

    private func dfs(_ node: TreeNode?) -> Int {
        guard let node = node else { return Int.min }
        let l = dfs(node.left)
        let r = dfs(node.right)
        let mx = max(max(l, r), node.val)
        if mx == node.val { ans += 1 }
        return mx
    }

    func countDominantNodes(_ root: TreeNode?) -> Int {
        ans = 0
        _ = dfs(root)
        return ans
    }
}
