// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init(_ val: Int = 0, _ left: TreeNode? = nil, _ right: TreeNode? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func correctBinaryTree(_ root: TreeNode?) -> TreeNode? {
        var seen = Set<ObjectIdentifier>()
        func dfs(_ node: TreeNode?) -> TreeNode? {
            guard let node = node else { return nil }
            if let r = node.right, seen.contains(ObjectIdentifier(r)) { return nil }
            seen.insert(ObjectIdentifier(node))
            node.right = dfs(node.right)
            node.left = dfs(node.left)
            return node
        }
        return dfs(root)
    }
}
