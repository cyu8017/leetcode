// LeetCode 0333 - Largest BST Subtree
// https://leetcode.com/problems/largest-bst-subtree/

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
    private var best = 0

    func largestBSTSubtree(_ root: TreeNode?) -> Int {
        best = 0
        dfs(root)
        return best
    }

    private func dfs(_ node: TreeNode?) -> (Bool, Int, Int, Int) {
        guard let node = node else {
            return (true, Int.max, Int.min, 0)
        }

        let left = dfs(node.left)
        let right = dfs(node.right)

        if left.0 && right.0 && left.2 < node.val && node.val < right.1 {
            let size = left.3 + right.3 + 1
            best = max(best, size)
            return (true, min(left.1, node.val), max(right.2, node.val), size)
        }

        return (false, 0, 0, 0)
    }
}
