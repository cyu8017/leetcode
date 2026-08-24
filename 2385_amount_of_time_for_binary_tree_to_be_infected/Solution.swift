// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

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
    func amountOfTime(_ root: TreeNode?, _ start: Int) -> Int {
        var g: [Int: [Int]] = [:]
        func build(_ node: TreeNode?, _ parent: TreeNode?) {
            guard let node = node else { return }
            if let parent = parent {
                g[node.val, default: []].append(parent.val)
                g[parent.val, default: []].append(node.val)
            }
            build(node.left, node)
            build(node.right, node)
        }
        build(root, nil)
        var vis = Set<Int>([start])
        var q: [(Int, Int)] = [(start, 0)]
        var ans = 0, i = 0
        while i < q.count {
            let (u, t) = q[i]; i += 1
            ans = max(ans, t)
            for nxt in g[u, default: []] where vis.insert(nxt).inserted {
                q.append((nxt, t + 1))
            }
        }
        return ans
    }
}
