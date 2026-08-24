// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

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
    private var cameras = 0

    func minCameraCover(_ root: TreeNode?) -> Int {
        cameras = 0
        let rootState = dfs(root)
        return cameras + (rootState == 0 ? 1 : 0)
    }

    private func dfs(_ node: TreeNode?) -> Int {
        guard let node = node else { return 1 }
        let left = dfs(node.left)
        let right = dfs(node.right)
        if left == 0 || right == 0 {
            cameras += 1
            return 2
        }
        if left == 2 || right == 2 { return 1 }
        return 0
    }
}
