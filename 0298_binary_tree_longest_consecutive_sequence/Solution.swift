// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

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
    func longestConsecutive(_ root: TreeNode?) -> Int {
        func dfs(_ node: TreeNode?, _ parent: TreeNode?, _ length: Int) -> Int {
            guard let node else {
                return 0
            }
            let current = parent != nil && parent!.val + 1 == node.val ? length + 1 : 1
            return max(current, dfs(node.left, node, current), dfs(node.right, node, current))
        }
        return dfs(root, nil, 0)
    }
}
