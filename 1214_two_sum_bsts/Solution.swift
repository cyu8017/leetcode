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

// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

class Solution {
    func twoSumBSTs(_ root1: TreeNode?, _ root2: TreeNode?, _ target: Int) -> Bool {
        var vals = Set<Int>()
        func collect(_ node: TreeNode?) {
            guard let node = node else { return }
            vals.insert(node.val)
            collect(node.left)
            collect(node.right)
        }
        collect(root1)
        func find(_ node: TreeNode?) -> Bool {
            guard let node = node else { return false }
            if vals.contains(target - node.val) { return true }
            return find(node.left) || find(node.right)
        }
        return find(root2)
    }
}
