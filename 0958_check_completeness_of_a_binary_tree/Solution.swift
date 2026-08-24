// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

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
    func isCompleteTree(_ root: TreeNode?) -> Bool {
        var q: [TreeNode?] = [root]
        var end = false
        var qi = 0
        while qi < q.count {
            let node = q[qi]
            qi += 1
            if node == nil {
                end = true
            } else {
                if end { return false }
                q.append(node!.left)
                q.append(node!.right)
            }
        }
        return true
    }
}
