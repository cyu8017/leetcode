// LeetCode 1382 - Balance a Binary Search Tree
// https://leetcode.com/problems/balance-a-binary-search-tree/

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
    func balanceBST(_ root: TreeNode?) -> TreeNode? {
        var nodes = [TreeNode]()
        func walk(_ x: TreeNode?) {
            guard let x = x else { return }
            walk(x.left); nodes.append(x); walk(x.right)
        }
        walk(root)
        func build(_ l: Int, _ r: Int) -> TreeNode? {
            if l >= r { return nil }
            let m = (l + r) / 2
            let x = nodes[m]
            x.left = build(l, m)
            x.right = build(m + 1, r)
            return x
        }
        return build(0, nodes.count)
    }
}
