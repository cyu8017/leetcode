// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

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
    func findNearestRightNode(_ root: TreeNode?, _ u: TreeNode?) -> TreeNode? {
        guard let root = root, let u = u else { return nil }
        var q = [root]
        while !q.isEmpty {
            let size = q.count
            for i in 0..<size {
                let node = q[i]
                if node === u {
                    return i + 1 < size ? q[i + 1] : nil
                }
                if let left = node.left { q.append(left) }
                if let right = node.right { q.append(right) }
            }
            q.removeFirst(size)
        }
        return nil
    }
}
