// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

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
    func smallestFromLeaf(_ root: TreeNode?) -> String {
        var best = "~"
        func dfs(_ node: TreeNode?, _ path: String) {
            guard let node = node else { return }
            let ch = Character(UnicodeScalar(UInt32(97 + node.val))!)
            let next = String(ch) + path
            if node.left == nil && node.right == nil {
                if next < best { best = next }
                return
            }
            dfs(node.left, next)
            dfs(node.right, next)
        }
        dfs(root, "")
        return best
    }
}
