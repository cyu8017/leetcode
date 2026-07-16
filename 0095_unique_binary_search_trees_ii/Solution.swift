// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

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
    func generateTrees(_ n: Int) -> [TreeNode?] {
        if n == 0 {
            return []
        }
        return build(1, n)
    }

    private func build(_ start: Int, _ end: Int) -> [TreeNode?] {
        if start > end {
            return [nil]
        }
        var trees = [TreeNode?]()
        for rootVal in start...end {
            let leftTrees = build(start, rootVal - 1)
            let rightTrees = build(rootVal + 1, end)
            for left in leftTrees {
                for right in rightTrees {
                    trees.append(TreeNode(rootVal, left, right))
                }
            }
        }
        return trees
    }
}
