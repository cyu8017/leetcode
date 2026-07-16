// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

class Solution {
    func findMode(_ root: TreeNode?) -> [Int] {
        var counts: [Int: Int] = [:]
        var best = 0

        func inorder(_ node: TreeNode?) {
            guard let node else {
                return
            }
            inorder(node.left)
            counts[node.val, default: 0] += 1
            best = max(best, counts[node.val]!)
            inorder(node.right)
        }

        inorder(root)
        return counts.filter { $0.value == best }.map(\.key)
    }
}

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
