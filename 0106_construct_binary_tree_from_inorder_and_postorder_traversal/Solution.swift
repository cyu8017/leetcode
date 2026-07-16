// LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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
    private var postIndex = 0
    private var postorder: [Int] = []
    private var index: [Int: Int] = [:]

    func buildTree(_ inorder: [Int], _ postorder: [Int]) -> TreeNode? {
        self.postorder = postorder
        self.postIndex = postorder.count - 1
        self.index = Dictionary(uniqueKeysWithValues: inorder.enumerated().map { ($0.element, $0.offset) })
        return build(0, inorder.count - 1)
    }

    private func build(_ left: Int, _ right: Int) -> TreeNode? {
        if left > right {
            return nil
        }
        let rootVal = postorder[postIndex]
        postIndex -= 1
        let mid = index[rootVal]!
        let root = TreeNode(rootVal)
        root.right = build(mid + 1, right)
        root.left = build(left, mid - 1)
        return root
    }
}