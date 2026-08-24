// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

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
    func findTarget(_ root: TreeNode?, _ k: Int) -> Bool {
        var seen = Set<Int>()
        func dfs(_ node: TreeNode?) -> Bool {
            guard let node else { return false }
            if seen.contains(k - node.val) { return true }
            seen.insert(node.val)
            return dfs(node.left) || dfs(node.right)
        }
        return dfs(root)
    }
}
