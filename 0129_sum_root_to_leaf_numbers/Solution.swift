// LeetCode 0129 - Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

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
    func sumNumbers(_ root: TreeNode?) -> Int {
        func dfs(_ node: TreeNode?, _ value: Int) -> Int {
            guard let node = node else { return 0 }
            let next = value * 10 + node.val
            if node.left == nil && node.right == nil {
                return next
            }
            return dfs(node.left, next) + dfs(node.right, next)
        }
        return dfs(root, 0)
    }
}