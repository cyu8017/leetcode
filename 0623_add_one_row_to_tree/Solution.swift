// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

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
    func addOneRow(_ root: TreeNode?, _ val: Int, _ depth: Int) -> TreeNode? {
        if depth == 1 { return TreeNode(val, root, nil) }
        func dfs(_ node: TreeNode?, _ current: Int) {
            guard let node else { return }
            if current == depth - 1 {
                node.left = TreeNode(val, node.left, nil)
                node.right = TreeNode(val, nil, node.right)
                return
            }
            dfs(node.left, current + 1)
            dfs(node.right, current + 1)
        }
        dfs(root, 1)
        return root
    }
}
