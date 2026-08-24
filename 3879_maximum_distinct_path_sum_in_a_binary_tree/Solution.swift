// LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

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
    private var g = [ObjectIdentifier: [TreeNode?]]()
    private var vis = [Int: Bool]()
    private var nodes = [TreeNode]()

    private func dfs(_ node: TreeNode?, _ p: TreeNode?) {
        guard let node = node else { return }
        g[ObjectIdentifier(node)] = [p, node.left, node.right]
        nodes.append(node)
        dfs(node.left, node)
        dfs(node.right, node)
    }

    private func dfs2(_ node: TreeNode?) -> Int {
        guard let node = node, vis[node.val] != true else { return 0 }
        vis[node.val] = true
        var best = 0
        if let nbrs = g[ObjectIdentifier(node)] {
            for nxt in nbrs { best = max(best, dfs2(nxt)) }
        }
        vis[node.val] = false
        return node.val + best
    }

    func maxSum(_ root: TreeNode?) -> Int {
        g = [:]
        vis = [:]
        nodes = []
        dfs(root, nil)
        var ans = Int.min
        for node in nodes {
            ans = max(ans, dfs2(node))
            vis = [:]
        }
        return ans
    }
}
