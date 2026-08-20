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

// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

class Solution {
    func btreeGameWinningMove(_ root: TreeNode?, _ n: Int, _ x: Int) -> Bool {
        var left = 0, right = 0
        func dfs(_ node: TreeNode?) -> Int {
            guard let node = node else { return 0 }
            let l = dfs(node.left), r = dfs(node.right)
            if node.val == x { left = l; right = r }
            return l + r + 1
        }
        _ = dfs(root)
        return max(left, right, n - left - right - 1) > n / 2
    }
}
