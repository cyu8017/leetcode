// LeetCode 3831 - Median Of A Binary Search Tree Level
// https://leetcode.com/problems/median-of-a-binary-search-tree-level/

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
    private var nums = [Int]()

    func levelMedian(_ root: TreeNode?, _ level: Int) -> Int {
        nums = []
        dfs(root, 0, level)
        if nums.isEmpty { return -1 }
        return nums[nums.count / 2]
    }

    private func dfs(_ node: TreeNode?, _ i: Int, _ level: Int) {
        guard let node = node else { return }
        dfs(node.left, i + 1, level)
        if i == level { nums.append(node.val) }
        dfs(node.right, i + 1, level)
    }
}
