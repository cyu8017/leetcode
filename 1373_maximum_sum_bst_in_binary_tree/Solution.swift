// LeetCode 1373 - Maximum Sum BST in Binary Tree
// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

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
    func maxSumBST(_ root: TreeNode?) -> Int {
        var ans = 0
        func dfs(_ node: TreeNode?) -> (Bool, Int, Int, Int) {
            guard let node = node else { return (true, Int.max, Int.min, 0) }
            let L = dfs(node.left), R = dfs(node.right)
            if L.0 && R.0 && L.2 < node.val && node.val < R.1 {
                let s = L.3 + R.3 + node.val
                ans = max(ans, s)
                return (true, min(L.1, node.val), max(R.2, node.val), s)
            }
            return (false, 0, 0, 0)
        }
        _ = dfs(root)
        return ans
    }
}
