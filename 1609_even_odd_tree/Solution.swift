// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

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
    func isEvenOddTree(_ root: TreeNode?) -> Bool {
        guard let root = root else { return true }
        var q = [root]
        var level = 0
        while !q.isEmpty {
            let size = q.count
            var prev = level % 2 == 0 ? Int.min : Int.max
            for i in 0..<size {
                let node = q[i]
                if node.val % 2 == level % 2 { return false }
                if level % 2 == 0 && node.val <= prev { return false }
                if level % 2 == 1 && node.val >= prev { return false }
                prev = node.val
                if let left = node.left { q.append(left) }
                if let right = node.right { q.append(right) }
            }
            q.removeFirst(size)
            level += 1
        }
        return true
    }
}
