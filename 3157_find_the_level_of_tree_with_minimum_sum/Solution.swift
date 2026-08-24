// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

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
    func minimumLevel(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        var q: [TreeNode] = [root]
        var s = Int.max
        var ans = 0
        var level = 1
        while !q.isEmpty {
            var t = 0
            var nq: [TreeNode] = []
            for node in q {
                t += node.val
                if let l = node.left { nq.append(l) }
                if let r = node.right { nq.append(r) }
            }
            if s > t {
                s = t
                ans = level
            }
            q = nq
            level += 1
        }
        return ans
    }
}
