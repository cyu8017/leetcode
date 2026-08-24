// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

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
    func averageOfSubtree(_ root: TreeNode?) -> Int {
        var ans = 0
        func dfs(_ node: TreeNode?) -> (Int, Int) {
            guard let node = node else { return (0, 0) }
            let L = dfs(node.left)
            let R = dfs(node.right)
            let sum = L.0 + R.0 + node.val
            let cnt = L.1 + R.1 + 1
            if sum / cnt == node.val { ans += 1 }
            return (sum, cnt)
        }
        _ = dfs(root)
        return ans
    }
}
