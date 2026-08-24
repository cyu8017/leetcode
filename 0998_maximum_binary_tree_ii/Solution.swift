// LeetCode 0998 - Maximum Binary Tree II
// https://leetcode.com/problems/maximum-binary-tree-ii/

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func insertIntoMaxTree(_ root: TreeNode?, _ val: Int) -> TreeNode? {
        if root == nil || val > root!.val {
            let node = TreeNode(val)
            node.left = root
            return node
        }
        root!.right = insertIntoMaxTree(root!.right, val)
        return root
    }
}
