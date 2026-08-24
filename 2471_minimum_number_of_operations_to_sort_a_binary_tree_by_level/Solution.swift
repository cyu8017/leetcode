// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

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
    func minimumOperations(_ root: TreeNode?) -> Int {
        guard let root else { return 0 }
        var ans = 0
        var q = [root]
        while !q.isEmpty {
            var nxt = [TreeNode]()
            var vals = [Int]()
            for node in q {
                vals.append(node.val)
                if let l = node.left { nxt.append(l) }
                if let r = node.right { nxt.append(r) }
            }
            let sorted = vals.sorted()
            var pos = [Int: Int]()
            for i in 0..<vals.count { pos[vals[i]] = i }
            for i in 0..<vals.count {
                if vals[i] != sorted[i] {
                    let j = pos[sorted[i]]!
                    vals.swapAt(i, j)
                    pos[vals[j]] = j
                    pos[vals[i]] = i
                    ans += 1
                }
            }
            q = nxt
        }
        return ans
    }
}
