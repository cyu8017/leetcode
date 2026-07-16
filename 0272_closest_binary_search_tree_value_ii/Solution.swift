// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

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
    func closestKValues(_ root: TreeNode?, _ target: Double, _ k: Int) -> [Int] {
        var values: [Int] = []
        inorder(root, &values)

        var lo = 0
        var hi = values.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if Double(values[mid]) < target {
                lo = mid + 1
            } else {
                hi = mid
            }
        }

        var left = lo - 1
        var right = lo
        var result: [Int] = []
        while result.count < k {
            if right >= values.count ||
                (left >= 0 && abs(Double(values[left]) - target) <= abs(Double(values[right]) - target)) {
                result.append(values[left])
                left -= 1
            } else {
                result.append(values[right])
                right += 1
            }
        }
        return result
    }

    private func inorder(_ node: TreeNode?, _ values: inout [Int]) {
        guard let node = node else { return }
        inorder(node.left, &values)
        values.append(node.val)
        inorder(node.right, &values)
    }
}
