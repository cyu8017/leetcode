// LeetCode 1530 - Number of Good Leaf Nodes Pairs
// https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init() { self.val = 0; self.left = nil; self.right = nil }
    init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val; self.left = left; self.right = right
    }
}

class Solution {
    func countPairs(_ root: TreeNode?, _ distance: Int) -> Int {
        var answer = 0
        func dfs(_ node: TreeNode?) -> [Int] {
            guard let node = node else { return [] }
            if node.left == nil && node.right == nil { return [1] }
            let left = dfs(node.left)
            let right = dfs(node.right)
            for a in left {
                for b in right where a + b <= distance {
                    answer += 1
                }
            }
            return (left + right).compactMap { d in
                let nd = d + 1
                return nd < distance ? nd : nil
            }
        }
        _ = dfs(root)
        return answer
    }
}
