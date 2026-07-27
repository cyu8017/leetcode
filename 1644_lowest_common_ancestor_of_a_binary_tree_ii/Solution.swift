// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

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
    func lowestCommonAncestor(_ root: TreeNode?, _ p: TreeNode?, _ q: TreeNode?) -> TreeNode? {
        var found = 0
        func dfs(_ node: TreeNode?) -> TreeNode? {
            guard let node = node else { return nil }
            let left = dfs(node.left)
            let right = dfs(node.right)
            if node === p || node === q {
                found += 1
                return node
            }
            if left != nil && right != nil { return node }
            return left ?? right
        }
        let ans = dfs(root)
        return found == 2 ? ans : nil
    }
}
