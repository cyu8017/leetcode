// LeetCode 0270 - Closest Binary Search Tree Value
// https://leetcode.com/problems/closest-binary-search-tree-value/

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
    func closestValue(_ root: TreeNode?, _ target: Double) -> Int {
        var closest = root!.val
        var current: TreeNode? = root
        while let node = current {
            if abs(Double(closest) - target) > abs(Double(node.val) - target) {
                closest = node.val
            }
            if Double(node.val) == target {
                return node.val
            }
            current = target < Double(node.val) ? node.left : node.right
        }
        return closest
    }
}
