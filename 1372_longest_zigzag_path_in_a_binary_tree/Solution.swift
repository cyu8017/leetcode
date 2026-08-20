// LeetCode 1372 - Longest ZigZag Path in a Binary Tree
// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

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
    func longestZigZag(_ root: TreeNode?) -> Int {
        var ans = 0
        func dfs(_ node: TreeNode?) -> (Int, Int) {
            guard let node = node else { return (-1, -1) }
            let l = dfs(node.left), r = dfs(node.right)
            let a = l.1 + 1, b = r.0 + 1
            ans = max(ans, a, b)
            return (a, b)
        }
        _ = dfs(root)
        return ans
    }
}
