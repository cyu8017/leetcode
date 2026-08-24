// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

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
    func kthLargestLevelSum(_ root: TreeNode?, _ k: Int) -> Int {
        guard let root else { return -1 }
        var sums = [Int]()
        var q = [root]
        while !q.isEmpty {
            var nxt = [TreeNode]()
            var s = 0
            for node in q {
                s += node.val
                if let l = node.left { nxt.append(l) }
                if let r = node.right { nxt.append(r) }
            }
            sums.append(s)
            q = nxt
        }
        sums.sort(by: >)
        if k > sums.count { return -1 }
        return sums[k - 1]
    }
}
