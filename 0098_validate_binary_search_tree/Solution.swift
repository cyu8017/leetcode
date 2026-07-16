// LeetCode 0098 - Validate Binary Search Tree
// https://leetcode.com/problems/validate-binary-search-tree/

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
    func isValidBST(_ root: TreeNode?) -> Bool {
        return valid(root, nil, nil)
    }

    private func valid(_ node: TreeNode?, _ low: Int?, _ high: Int?) -> Bool {
        guard let node = node else {
            return true
        }
        if let low = low, !(low < node.val) {
            return false
        }
        if let high = high, !(node.val < high) {
            return false
        }
        return valid(node.left, low, node.val) && valid(node.right, node.val, high)
    }
}
