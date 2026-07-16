// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init(_ val: Int = 0, _ left: TreeNode? = nil, _ right: TreeNode? = nil) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func pathSum(_ root: TreeNode?, _ targetSum: Int) -> Int {
        var prefixCounts: [Int: Int] = [0: 1]
        return dfs(root, 0, targetSum, &prefixCounts)
    }

    private func dfs(
        _ node: TreeNode?,
        _ current: Int,
        _ targetSum: Int,
        _ prefixCounts: inout [Int: Int]
    ) -> Int {
        guard let node else {
            return 0
        }

        let updated = current + node.val
        var total = prefixCounts[updated - targetSum, default: 0]
        prefixCounts[updated, default: 0] += 1
        total += dfs(node.left, updated, targetSum, &prefixCounts)
        total += dfs(node.right, updated, targetSum, &prefixCounts)
        prefixCounts[updated, default: 0] -= 1
        return total
    }
}
