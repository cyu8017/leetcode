// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

public class RopeTreeNode {
    public var len: Int
    public var val: Character
    public var left: RopeTreeNode?
    public var right: RopeTreeNode?
    public init() { self.len = 0; self.val = "\0"; self.left = nil; self.right = nil }
    public init(_ val: Character) { self.len = 0; self.val = val; self.left = nil; self.right = nil }
}

class Solution {
    func getKthCharacter(_ root: RopeTreeNode, _ k: Int) -> Character {
        dfs(root, k)
    }

    private func dfs(_ node: RopeTreeNode, _ kk: Int) -> Character {
        if node.left == nil && node.right == nil { return node.val }
        var leftLen = 0
        if let left = node.left {
            leftLen = left.len > 0 ? left.len : 1
        }
        if kk <= leftLen { return dfs(node.left!, kk) }
        return dfs(node.right!, kk - leftLen)
    }
}
