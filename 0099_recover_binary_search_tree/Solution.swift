// LeetCode 0099 - Recover Binary Search Tree
// https://leetcode.com/problems/recover-binary-search-tree/

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
    func recoverTree(_ root: TreeNode?) {
        var first: TreeNode?
        var second: TreeNode?
        var previous: TreeNode?
        var stack: [TreeNode] = []
        var current = root

        while current != nil || !stack.isEmpty {
            while let node = current {
                stack.append(node)
                current = node.left
            }
            let node = stack.removeLast()
            if let previous = previous, previous.val > node.val {
                if first == nil {
                    first = previous
                }
                second = node
            }
            previous = node
            current = node.right
        }

        if let first = first, let second = second {
            let temp = first.val
            first.val = second.val
            second.val = temp
        }
    }
}
