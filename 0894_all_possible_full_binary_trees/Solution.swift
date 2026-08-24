// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

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
    private var memo = [Int: [TreeNode]]()

    func allPossibleFBT(_ n: Int) -> [TreeNode?] {
        return build(n)
    }

    private func build(_ nodes: Int) -> [TreeNode] {
        if let cached = memo[nodes] { return cached }
        var res = [TreeNode]()
        if nodes % 2 == 0 {
            memo[nodes] = res
            return res
        }
        if nodes == 1 {
            res.append(TreeNode(0))
            memo[nodes] = res
            return res
        }
        var left = 1
        while left < nodes {
            let right = nodes - 1 - left
            for L in build(left) {
                for R in build(right) {
                    res.append(TreeNode(0, L, R))
                }
            }
            left += 2
        }
        memo[nodes] = res
        return res
    }
}
