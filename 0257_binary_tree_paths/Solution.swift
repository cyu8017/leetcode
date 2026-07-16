// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

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
    func binaryTreePaths(_ root: TreeNode?) -> [String] {
        var result: [String] = []
        dfs(root, [], &result)
        return result
    }

    private func dfs(_ node: TreeNode?, _ path: [String], _ result: inout [String]) {
        guard let node = node else {
            return
        }
        var nextPath = path
        nextPath.append(String(node.val))
        if node.left == nil && node.right == nil {
            result.append(nextPath.joined(separator: "->"))
            return
        }
        dfs(node.left, nextPath, &result)
        dfs(node.right, nextPath, &result)
    }
}
