// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

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
    func constructMaximumBinaryTree(_ nums: [Int]) -> TreeNode? {
        func build(_ left: Int, _ right: Int) -> TreeNode? {
            if left > right { return nil }
            var mid = left
            for i in left...right where nums[i] > nums[mid] { mid = i }
            return TreeNode(nums[mid], build(left, mid - 1), build(mid + 1, right))
        }
        return build(0, nums.count - 1)
    }
}
