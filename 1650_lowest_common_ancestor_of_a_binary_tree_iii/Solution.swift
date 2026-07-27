// LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

class Node {
    var val: Int
    var left: Node?
    var right: Node?
    var parent: Node?
    init(_ val: Int = 0) {
        self.val = val
    }
}

class Solution {
    func lowestCommonAncestor(_ p: Node?, _ q: Node?) -> Node? {
        var a = p
        var b = q
        while a !== b {
            a = a != nil ? a?.parent : q
            b = b != nil ? b?.parent : p
        }
        return a
    }
}
