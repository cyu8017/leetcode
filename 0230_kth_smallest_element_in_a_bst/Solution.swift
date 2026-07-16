// LeetCode 0230 - Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

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
    func kthSmallest(_ root: TreeNode?, _ k: Int) -> Int {
        var stack: [TreeNode] = []
        var current = root
        var remaining = k

        while current != nil || !stack.isEmpty {
            while let node = current {
                stack.append(node)
                current = node.left
            }
            current = stack.removeLast()
            remaining -= 1
            if remaining == 0 {
                return current!.val
            }
            current = current?.right
        }

        return -1
    }
}
