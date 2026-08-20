// LeetCode 1457 - Pseudo-Palindromic Paths in a Binary Tree
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

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
    func pseudoPalindromicPaths (_ root: TreeNode?) -> Int {
        func dfs(_ node: TreeNode?, _ mask: Int) -> Int {
            guard let node = node else { return 0 }
            let mask = mask ^ (1 << node.val)
            if node.left == nil && node.right == nil {
                return mask & (mask - 1) == 0 ? 1 : 0
            }
            return dfs(node.left, mask) + dfs(node.right, mask)
        }
        return dfs(root, 0)
    }
}
