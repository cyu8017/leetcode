// LeetCode 0637 - Average of Levels in Binary Tree
// https://leetcode.com/problems/average-of-levels-in-binary-tree/

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
    func averageOfLevels(_ root: TreeNode?) -> [Double] {
        guard let root else { return [] }
        var result = [Double]()
        var queue = [root]
        var idx = 0
        while idx < queue.count {
            let count = queue.count - idx
            var total = 0
            for _ in 0..<count {
                let node = queue[idx]
                idx += 1
                total += node.val
                if let left = node.left { queue.append(left) }
                if let right = node.right { queue.append(right) }
            }
            result.append(Double(total) / Double(count))
        }
        return result
    }
}
