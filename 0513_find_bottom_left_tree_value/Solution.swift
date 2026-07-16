// LeetCode 0513 - Find Bottom Left Tree Value
// https://leetcode.com/problems/find-bottom-left-tree-value/

class Solution {
    func findBottomLeftValue(_ root: TreeNode?) -> Int {
        guard let root = root else {
            return 0
        }

        var queue = [root]
        var leftmost = root.val

        while !queue.isEmpty {
            let levelSize = queue.count
            for index in 0..<levelSize {
                let node = queue.removeFirst()
                if index == 0 {
                    leftmost = node.val
                }
                if let left = node.left {
                    queue.append(left)
                }
                if let right = node.right {
                    queue.append(right)
                }
            }
        }

        return leftmost
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
