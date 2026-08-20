// LeetCode 1339 - Maximum Product of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

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
    func maxProduct(_ root: TreeNode?) -> Int {
        var sums = [Int]()
        func total(_ node: TreeNode?) -> Int {
            guard let node = node else { return 0 }
            let value = node.val + total(node.left) + total(node.right)
            sums.append(value)
            return value
        }
        let whole = total(root)
        return sums.map { $0 * (whole - $0) }.max()! % 1_000_000_007
    }
}
