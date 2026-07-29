// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

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
    func sumRootToLeaf(_ root: TreeNode?) -> Int {
        func dfs(_ node: TreeNode?, _ value: Int) -> Int {
            guard let node = node else { return 0 }
            let value = value * 2 + node.val
            if node.left == nil && node.right == nil { return value }
            return dfs(node.left, value) + dfs(node.right, value)
        }
        return dfs(root, 0)
    }
}
