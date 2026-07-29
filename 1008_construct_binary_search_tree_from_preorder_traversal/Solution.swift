// LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

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
    func bstFromPreorder(_ preorder: [Int]) -> TreeNode? {
        var i = 0
        func build(_ bound: Int) -> TreeNode? {
            if i == preorder.count || preorder[i] > bound { return nil }
            let root = TreeNode(preorder[i])
            i += 1
            root.left = build(root.val)
            root.right = build(bound)
            return root
        }
        return build(Int.max)
    }
}
