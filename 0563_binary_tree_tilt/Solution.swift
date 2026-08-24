// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

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
    func findTilt(_ root: TreeNode?) -> Int {
        var total = 0
        func subtreeSum(_ node: TreeNode?) -> Int {
            guard let node else { return 0 }
            let left = subtreeSum(node.left)
            let right = subtreeSum(node.right)
            total += abs(left - right)
            return node.val + left + right
        }
        _ = subtreeSum(root)
        return total
    }
}
