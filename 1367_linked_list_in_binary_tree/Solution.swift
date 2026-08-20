// LeetCode 1367 - Linked List in Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { self.val = 0; self.next = nil }
    init(_ val: Int) { self.val = val; self.next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

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
    func isSubPath(_ head: ListNode?, _ root: TreeNode?) -> Bool {
        func match(_ a: ListNode?, _ b: TreeNode?) -> Bool {
            if a == nil { return true }
            guard let a = a, let b = b, a.val == b.val else { return false }
            return match(a.next, b.left) || match(a.next, b.right)
        }
        guard let root = root else { return false }
        return match(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right)
    }
}
