// LeetCode 0107 - Binary Tree Level Order Traversal II
// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

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
    func levelOrderBottom(_ root: TreeNode?) -> [[Int]] {
        guard let root = root else {
            return []
        }

        var result = [[Int]]()
        var queue = [root]

        while !queue.isEmpty {
            let size = queue.count
            var level = [Int]()
            for _ in 0..<size {
                let node = queue.removeFirst()
                level.append(node.val)
                if let left = node.left {
                    queue.append(left)
                }
                if let right = node.right {
                    queue.append(right)
                }
            }
            result.append(level)
        }

        result.reverse()
        return result
    }
}
