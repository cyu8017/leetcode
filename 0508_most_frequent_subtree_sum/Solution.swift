// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

class Solution {
    func findFrequentTreeSum(_ root: TreeNode?) -> [Int] {
        var counts: [Int: Int] = [:]

        func subtreeSum(_ node: TreeNode?) -> Int {
            guard let node else {
                return 0
            }
            let total = node.val + subtreeSum(node.left) + subtreeSum(node.right)
            counts[total, default: 0] += 1
            return total
        }

        subtreeSum(root)
        if counts.isEmpty {
            return []
        }
        let best = counts.values.max()!
        return counts.filter { $0.value == best }.map(\.key).sorted()
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
