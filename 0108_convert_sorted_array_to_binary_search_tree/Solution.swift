// LeetCode 0108 - Convert Sorted Array to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

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
    func sortedArrayToBST(_ nums: [Int]) -> TreeNode? {
        func build(_ left: Int, _ right: Int) -> TreeNode? {
            if left > right {
                return nil
            }
            let mid = (left + right + 1) / 2
            let root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        }
        return build(0, nums.count - 1)
    }
}
