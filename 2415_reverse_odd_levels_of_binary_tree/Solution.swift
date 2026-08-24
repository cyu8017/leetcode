// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

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
    func reverseOddLevels(_ root: TreeNode?) -> TreeNode? {
        func dfs(_ a: TreeNode?, _ b: TreeNode?, _ level: Int) {
            guard let a = a, let b = b else { return }
            if level % 2 == 1 {
                let tmp = a.val
                a.val = b.val
                b.val = tmp
            }
            dfs(a.left, b.right, level + 1)
            dfs(a.right, b.left, level + 1)
        }
        if let root = root { dfs(root.left, root.right, 1) }
        return root
    }
}
