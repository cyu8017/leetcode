// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

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
    func getDirections(_ root: TreeNode?, _ startValue: Int, _ destValue: Int) -> String {
        var ps = [Character]()
        var pd = [Character]()
        _ = path(root, startValue, &ps)
        _ = path(root, destValue, &pd)
        var i = 0
        while i < ps.count && i < pd.count && ps[i] == pd[i] { i += 1 }
        return String(repeating: "U", count: ps.count - i) + String(pd[i...])
    }

    private func path(_ node: TreeNode?, _ target: Int, _ p: inout [Character]) -> Bool {
        guard let node = node else { return false }
        if node.val == target { return true }
        p.append("L")
        if path(node.left, target, &p) { return true }
        p[p.count - 1] = "R"
        if path(node.right, target, &p) { return true }
        p.removeLast()
        return false
    }
}
