// LeetCode 0102 - Binary Tree Level Order Traversal
// https://leetcode.com/problems/binary-tree-level-order-traversal/

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
    func levelOrder(_ root: TreeNode?) -> [[Int]] {
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

        return result
    }
}
