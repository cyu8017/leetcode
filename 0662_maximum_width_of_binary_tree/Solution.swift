// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

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
    func widthOfBinaryTree(_ root: TreeNode?) -> Int {
        guard let root else { return 0 }
        var queue: [(TreeNode, Int)] = [(root, 0)]
        var idx = 0
        var best = 0
        while idx < queue.count {
            let left = queue[idx].1
            let size = queue.count - idx
            for _ in 0..<size {
                let (node, i) = queue[idx]
                idx += 1
                best = max(best, i - left + 1)
                if let l = node.left { queue.append((l, i * 2)) }
                if let r = node.right { queue.append((r, i * 2 + 1)) }
            }
        }
        return best
    }
}
