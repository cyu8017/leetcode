// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func kthLargestPerfectSubtree(_ root: TreeNode?, _ k: Int) -> Int {
        var sizes = [Int]()
        @discardableResult
        func dfs(_ node: TreeNode?) -> (Int, Int, Bool) {
            guard let node else { return (0, 0, true) }
            let L = dfs(node.left)
            let R = dfs(node.right)
            let sz = L.1 + R.1 + 1
            let perf = L.2 && R.2 && L.0 == R.0
            if perf { sizes.append(sz) }
            return (max(L.0, R.0) + 1, sz, perf)
        }
        _ = dfs(root)
        sizes.sort(by: >)
        if k > sizes.count { return -1 }
        return sizes[k - 1]
    }
}
