// LeetCode 0094 - Binary Tree Inorder Traversal
// https://leetcode.com/problems/binary-tree-inorder-traversal/

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
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        var result = [Int]()
        var stack = [TreeNode]()
        var current = root
        while current != nil || !stack.isEmpty {
            while let node = current {
                stack.append(node)
                current = node.left
            }
            let node = stack.removeLast()
            result.append(node.val)
            current = node.right
        }
        return result
    }
}
