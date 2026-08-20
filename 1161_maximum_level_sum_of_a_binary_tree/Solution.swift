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

// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

class Solution {
    func maxLevelSum(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        var q: [TreeNode] = [root]
        var level = 1, bestLevel = 1, bestSum = root.val
        while !q.isEmpty {
            let sum = q.reduce(0) { $0 + $1.val }
            if sum > bestSum { bestSum = sum; bestLevel = level }
            var next: [TreeNode] = []
            for node in q {
                if let l = node.left { next.append(l) }
                if let r = node.right { next.append(r) }
            }
            q = next
            level += 1
        }
        return bestLevel
    }
}
