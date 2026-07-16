// LeetCode 0404 - Sum of Left Leaves
// https://leetcode.com/problems/sum-of-left-leaves/

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
    func sumOfLeftLeaves(_ root: TreeNode?) -> Int {
        guard let root = root else {
            return 0
        }

        var total = 0
        if let left = root.left, left.left == nil, left.right == nil {
            total += left.val
        } else {
            total += sumOfLeftLeaves(root.left)
        }

        total += sumOfLeftLeaves(root.right)
        return total
    }
}
