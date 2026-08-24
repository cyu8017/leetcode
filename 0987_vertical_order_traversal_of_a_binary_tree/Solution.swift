// LeetCode 0987 - Vertical Order Traversal of a Binary Tree
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func verticalTraversal(_ root: TreeNode?) -> [[Int]] {
        var nodes = [(col: Int, row: Int, val: Int)]()
        func dfs(_ node: TreeNode?, _ row: Int, _ col: Int) {
            guard let node = node else { return }
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        }
        dfs(root, 0, 0)
        nodes.sort {
            if $0.col != $1.col { return $0.col < $1.col }
            if $0.row != $1.row { return $0.row < $1.row }
            return $0.val < $1.val
        }
        var result = [[Int]]()
        var lastCol: Int?
        for n in nodes {
            if lastCol != n.col {
                result.append([])
                lastCol = n.col
            }
            result[result.count - 1].append(n.val)
        }
        return result
    }
}
