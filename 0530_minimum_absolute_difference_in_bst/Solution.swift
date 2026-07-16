// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

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
    func getMinimumDifference(_ root: TreeNode?) -> Int {
        var previous: Int?
        var best = Int.max

        func inorder(_ node: TreeNode?) {
            guard let node else { return }
            inorder(node.left)
            if let prev = previous {
                best = min(best, node.val - prev)
            }
            previous = node.val
            inorder(node.right)
        }

        inorder(root)
        return best
    }
}
