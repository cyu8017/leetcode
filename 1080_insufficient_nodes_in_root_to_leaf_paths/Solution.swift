// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

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
    func sufficientSubset(_ root: TreeNode?, _ limit: Int) -> TreeNode? {
        func dfs(_ node: TreeNode?, _ pathSum: Int) -> TreeNode? {
            guard let node = node else { return nil }
            let pathSum = pathSum + node.val
            if node.left == nil && node.right == nil {
                return pathSum >= limit ? node : nil
            }
            node.left = dfs(node.left, pathSum)
            node.right = dfs(node.right, pathSum)
            if node.left == nil && node.right == nil {
                return nil
            }
            return node
        }
        return dfs(root, 0)
    }
}
