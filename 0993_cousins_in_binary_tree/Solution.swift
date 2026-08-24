// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func isCousins(_ root: TreeNode?, _ x: Int, _ y: Int) -> Bool {
        var depth = [Int: Int]()
        var parent = [Int: ObjectIdentifier]()
        func dfs(_ node: TreeNode?, _ p: TreeNode?, _ d: Int) {
            guard let node = node else { return }
            depth[node.val] = d
            if let p = p { parent[node.val] = ObjectIdentifier(p) }
            dfs(node.left, node, d + 1)
            dfs(node.right, node, d + 1)
        }
        dfs(root, nil, 0)
        return depth[x] == depth[y] && parent[x] != parent[y]
    }
}
