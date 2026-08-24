// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val; self.left = left; self.right = right
    }
}

class Solution {
    func closestNodes(_ root: TreeNode?, _ queries: [Int]) -> [[Int]] {
        var vals = [Int]()
        func inorder(_ node: TreeNode?) {
            guard let node else { return }
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        }
        inorder(root)
        var ans = [[Int]]()
        for q in queries {
            var lo = 0, hi = vals.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if vals[mid] < q { lo = mid + 1 }
                else { hi = mid }
            }
            let mx = lo < vals.count ? vals[lo] : -1
            var mn = -1
            if lo < vals.count && vals[lo] == q { mn = q }
            else if lo > 0 { mn = vals[lo - 1] }
            ans.append([mn, mx])
        }
        return ans
    }
}
