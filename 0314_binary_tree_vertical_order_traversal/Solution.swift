// LeetCode 0314 - Binary Tree Vertical Order Traversal
// https://leetcode.com/problems/binary-tree-vertical-order-traversal/

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
    func verticalOrder(_ root: TreeNode?) -> [[Int]] {
        guard let root else {
            return []
        }

        var columns: [Int: [Int]] = [:]
        var queue: [(TreeNode, Int)] = [(root, 0)]
        var minCol = 0
        var maxCol = 0
        while !queue.isEmpty {
            let (node, column) = queue.removeFirst()
            minCol = min(minCol, column)
            maxCol = max(maxCol, column)
            columns[column, default: []].append(node.val)
            if let left = node.left {
                queue.append((left, column - 1))
            }
            if let right = node.right {
                queue.append((right, column + 1))
            }
        }
        return (minCol...maxCol).map { columns[$0] ?? [] }
    }
}
