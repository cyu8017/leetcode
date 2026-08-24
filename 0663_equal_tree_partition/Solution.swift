// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

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
    func checkEqualTree(_ root: TreeNode?) -> Bool {
        var subtreeSums = [Int]()
        func dfs(_ node: TreeNode?) -> Int {
            guard let node else { return 0 }
            let total = node.val + dfs(node.left) + dfs(node.right)
            subtreeSums.append(total)
            return total
        }
        let total = dfs(root)
        if !subtreeSums.isEmpty { subtreeSums.removeLast() }
        if total % 2 != 0 { return false }
        return subtreeSums.contains(total / 2)
    }
}
