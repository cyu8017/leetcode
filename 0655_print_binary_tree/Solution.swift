// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

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
    func printTree(_ root: TreeNode?) -> [[String]] {
        func height(_ node: TreeNode?) -> Int {
            guard let node else { return -1 }
            return 1 + max(height(node.left), height(node.right))
        }
        let h = height(root)
        let rows = h + 1
        let cols = (1 << (h + 1)) - 1
        var res = Array(repeating: Array(repeating: "", count: cols), count: rows)
        func place(_ node: TreeNode?, _ r: Int, _ c: Int) {
            guard let node else { return }
            res[r][c] = String(node.val)
            if r == h { return }
            let offset = 1 << (h - r - 1)
            place(node.left, r + 1, c - offset)
            place(node.right, r + 1, c + offset)
        }
        place(root, 0, (cols - 1) / 2)
        return res
    }
}
