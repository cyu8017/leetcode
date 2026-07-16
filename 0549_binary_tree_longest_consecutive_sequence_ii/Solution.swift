// LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

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
    func longestConsecutive(_ root: TreeNode?) -> Int {
        var best = 0

        func dfs(_ node: TreeNode?) -> (Int, Int) {
            guard let node else { return (0, 0) }

            let (leftInc, leftDec) = dfs(node.left)
            let (rightInc, rightDec) = dfs(node.right)

            var inc = 1
            var dec = 1
            if let left = node.left {
                if left.val == node.val + 1 {
                    inc = max(inc, leftInc + 1)
                } else if left.val == node.val - 1 {
                    dec = max(dec, leftDec + 1)
                }
            }
            if let right = node.right {
                if right.val == node.val + 1 {
                    inc = max(inc, rightInc + 1)
                } else if right.val == node.val - 1 {
                    dec = max(dec, rightDec + 1)
                }
            }

            if let left = node.left, let right = node.right {
                if left.val + 1 == node.val && node.val == right.val - 1 {
                    best = max(best, leftDec + 1 + rightInc)
                }
                if left.val - 1 == node.val && node.val == right.val + 1 {
                    best = max(best, leftInc + 1 + rightDec)
                }
            }

            best = max(best, inc, dec)
            return (inc, dec)
        }

        _ = dfs(root)
        return best
    }
}
