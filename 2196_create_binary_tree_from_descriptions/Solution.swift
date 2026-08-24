// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

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
    func createBinaryTree(_ descriptions: [[Int]]) -> TreeNode? {
        var nodes = [Int: TreeNode]()
        var child = Set<Int>()
        for d in descriptions {
            let p = d[0], c = d[1], isLeft = d[2]
            if nodes[p] == nil { nodes[p] = TreeNode(p) }
            if nodes[c] == nil { nodes[c] = TreeNode(c) }
            if isLeft == 1 { nodes[p]!.left = nodes[c] }
            else { nodes[p]!.right = nodes[c] }
            child.insert(c)
        }
        for (k, v) in nodes where !child.contains(k) { return v }
        return nil
    }
}
