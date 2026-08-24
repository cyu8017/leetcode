// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val; self.left = left; self.right = right
    }
}

class Solution {
    func heightOfTree(_ root: TreeNode?) -> Int {
        if root == nil { return -1 }
        return dfs(root)
    }

    private func dfs(_ node: TreeNode?) -> Int {
        guard let node = node else { return -1 }
        if let l = node.left, l.right === node { return dfs(node.right) + 1 }
        if let r = node.right, r.left === node { return dfs(node.left) + 1 }
        return max(dfs(node.left), dfs(node.right)) + 1
    }
}
