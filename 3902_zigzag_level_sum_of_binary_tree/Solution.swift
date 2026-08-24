// LeetCode 3902 - Zigzag Level Sum Of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

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
    func zigzagLevelSum(_ root: TreeNode?) -> [Int] {
        guard let root = root else { return [] }
        var ans = [Int]()
        var q = [root]
        var left = true
        while !q.isEmpty {
            var nq = [TreeNode]()
            for node in q {
                if let l = node.left { nq.append(l) }
                if let r = node.right { nq.append(r) }
            }
            let m = q.count
            var s = 0
            for i in 0..<m {
                let node = left ? q[i] : q[m - i - 1]
                let child = left ? node.left : node.right
                if child == nil { break }
                s += node.val
            }
            ans.append(s)
            left = !left
            q = nq
        }
        return ans
    }
}
