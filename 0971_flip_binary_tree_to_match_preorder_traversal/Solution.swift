// LeetCode 0971 - Flip Binary Tree To Match Preorder Traversal
// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

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
    func flipMatchVoyage(_ root: TreeNode?, _ voyage: [Int]) -> [Int] {
        var i = 0
        var ans = [Int]()
        func dfs(_ node: TreeNode?) -> Bool {
            guard let node = node else { return true }
            if node.val != voyage[i] { return false }
            i += 1
            if let left = node.left, left.val != voyage[i] {
                ans.append(node.val)
                return dfs(node.right) && dfs(node.left)
            }
            return dfs(node.left) && dfs(node.right)
        }
        return dfs(root) ? ans : [-1]
    }
}
