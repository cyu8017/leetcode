// LeetCode 1315 - Sum of Nodes with Even-Valued Grandparent
// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

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
    func sumEvenGrandparent(_ root: TreeNode?) -> Int {
        func dfs(_ node: TreeNode?, _ parent: Int, _ grand: Int) -> Int {
            guard let node = node else { return 0 }
            let add = grand % 2 == 0 ? node.val : 0
            return add + dfs(node.left, node.val, parent) + dfs(node.right, node.val, parent)
        }
        return dfs(root, 1, 1)
    }
}
