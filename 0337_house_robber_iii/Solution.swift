// LeetCode 0337 - House Robber III
// https://leetcode.com/problems/house-robber-iii/

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
    func rob(_ root: TreeNode?) -> Int {
        maxPair(dfs(root))
    }

    private func dfs(_ node: TreeNode?) -> (Int, Int) {
        guard let node = node else {
            return (0, 0)
        }

        let left = dfs(node.left)
        let right = dfs(node.right)
        let withRob = node.val + left.1 + right.1
        let withoutRob = max(left.0, left.1) + max(right.0, right.1)
        return (withRob, withoutRob)
    }

    private func maxPair(_ pair: (Int, Int)) -> Int {
        max(pair.0, pair.1)
    }
}
