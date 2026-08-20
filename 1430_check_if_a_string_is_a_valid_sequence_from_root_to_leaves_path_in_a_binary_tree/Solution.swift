// LeetCode 1430 - Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
// https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

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
    func isValidSequence(_ root: TreeNode?, _ arr: [Int]) -> Bool {
        func visit(_ node: TreeNode?, _ index: Int) -> Bool {
            guard let node = node, index < arr.count, node.val == arr[index] else { return false }
            if node.left == nil && node.right == nil { return index == arr.count - 1 }
            return visit(node.left, index + 1) || visit(node.right, index + 1)
        }
        return visit(root, 0)
    }
}
