// LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
    private var preIndex = 0
    private var preorder: [Int] = []
    private var index: [Int: Int] = [:]

    func buildTree(_ preorder: [Int], _ inorder: [Int]) -> TreeNode? {
        self.preorder = preorder
        self.preIndex = 0
        self.index = Dictionary(uniqueKeysWithValues: inorder.enumerated().map { ($0.element, $0.offset) })
        return build(0, inorder.count - 1)
    }

    private func build(_ left: Int, _ right: Int) -> TreeNode? {
        if left > right {
            return nil
        }
        let rootVal = preorder[preIndex]
        preIndex += 1
        let mid = index[rootVal]!
        let root = TreeNode(rootVal)
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root
    }
}