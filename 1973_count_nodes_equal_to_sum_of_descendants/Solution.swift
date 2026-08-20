// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

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
    func equalToDescendants(_ root: TreeNode?) -> Int {
        var ans = 0
        func dfs(_ node: TreeNode?) -> Int {
            guard let node = node else { return 0 }
            let total = dfs(node.left) + dfs(node.right)
            if total == node.val { ans += 1 }
            return total + node.val
        }
        _ = dfs(root)
        return ans
    }
}
