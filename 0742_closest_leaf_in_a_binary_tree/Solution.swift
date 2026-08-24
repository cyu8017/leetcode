// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

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
    func findClosestLeaf(_ root: TreeNode?, _ k: Int) -> Int {
        var graph = [Int: [Int]]()
        var leaves = Set<Int>()
        func dfs(_ node: TreeNode?, _ parent: Int?) {
            guard let node else { return }
            if let parent { graph[node.val, default: []].append(parent); graph[parent, default: []].append(node.val) }
            if node.left == nil && node.right == nil { leaves.insert(node.val) }
            dfs(node.left, node.val)
            dfs(node.right, node.val)
        }
        dfs(root, nil)
        var queue = [k]
        var seen = Set([k])
        var idx = 0
        while idx < queue.count {
            let cur = queue[idx]
            idx += 1
            if leaves.contains(cur) { return cur }
            for nei in graph[cur] ?? [] where seen.insert(nei).inserted {
                queue.append(nei)
            }
        }
        return -1
    }
}
