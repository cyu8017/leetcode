// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

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
    func findSecondMinimumValue(_ root: TreeNode?) -> Int {
        guard let root else { return -1 }
        var ans = -1
        let rootVal = root.val
        func dfs(_ node: TreeNode?) {
            guard let node else { return }
            if node.val > rootVal {
                if ans == -1 || node.val < ans { ans = node.val }
                return
            }
            dfs(node.left)
            dfs(node.right)
        }
        dfs(root)
        return ans
    }
}
