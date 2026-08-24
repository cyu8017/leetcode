// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

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
    private var ans = 0
    private var k = 0

    func countGreatEnoughNodes(_ root: TreeNode?, _ k: Int) -> Int {
        self.k = k
        self.ans = 0
        _ = dfs(root)
        return ans
    }

    private func dfs(_ node: TreeNode?) -> [Int] {
        guard let node = node else { return [] }
        var vals = merge(dfs(node.left), dfs(node.right))
        var smaller = 0
        for v in vals where v < node.val { smaller += 1 }
        if smaller >= k { ans += 1 }
        vals.append(node.val)
        vals.sort()
        if vals.count > k { vals = Array(vals.prefix(k)) }
        return vals
    }

    private func merge(_ a: [Int], _ b: [Int]) -> [Int] {
        var i = 0, j = 0, out: [Int] = []
        while i < a.count && j < b.count && out.count < k {
            if a[i] < b[j] { out.append(a[i]); i += 1 } else { out.append(b[j]); j += 1 }
        }
        while i < a.count && out.count < k { out.append(a[i]); i += 1 }
        while j < b.count && out.count < k { out.append(b[j]); j += 1 }
        return out
    }
}
