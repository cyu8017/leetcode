// LeetCode 2236 - Root Equals Sum of Children
// https://leetcode.com/problems/root-equals-sum-of-children/

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
    func checkTree(_ root: TreeNode?) -> Bool {
        guard let root = root, let L = root.left, let R = root.right else { return false }
        return root.val == L.val + R.val
    }
}
