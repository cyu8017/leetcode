// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

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
    func constructFromPrePost(_ preorder: [Int], _ postorder: [Int]) -> TreeNode? {
        var postIndex = [Int: Int]()
        for i in 0..<postorder.count { postIndex[postorder[i]] = i }
        func build(_ preLo: Int, _ preHi: Int, _ postLo: Int, _ postHi: Int) -> TreeNode? {
            if preLo > preHi { return nil }
            let root = TreeNode(preorder[preLo])
            if preLo == preHi { return root }
            let leftVal = preorder[preLo + 1]
            let leftPost = postIndex[leftVal]!
            let leftSize = leftPost - postLo + 1
            root.left = build(preLo + 1, preLo + leftSize, postLo, leftPost)
            root.right = build(preLo + leftSize + 1, preHi, leftPost + 1, postHi - 1)
            return root
        }
        let n = preorder.count
        return build(0, n - 1, 0, n - 1)
    }
}
