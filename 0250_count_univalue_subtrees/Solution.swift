// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

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
    private var count = 0

    func countUnivalSubtrees(_ root: TreeNode?) -> Int {
        count = 0
        dfs(root)
        return count
    }

    private func dfs(_ node: TreeNode?) -> Bool {
        guard let node = node else {
            return true
        }
        let leftOk = dfs(node.left)
        let rightOk = dfs(node.right)
        if !leftOk || !rightOk {
            return false
        }
        if let left = node.left, left.val != node.val {
            return false
        }
        if let right = node.right, right.val != node.val {
            return false
        }
        count += 1
        return true
    }
}
