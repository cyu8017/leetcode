// LeetCode 1367 - Linked List in Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isSubPath(head: ListNode?, root: TreeNode?): Boolean {
        if (root == null) return false
        return match(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right)
    }

    private fun match(a: ListNode?, b: TreeNode?): Boolean {
        if (a == null) return true
        if (b == null || a.`val` != b.`val`) return false
        return match(a.next, b.left) || match(a.next, b.right)
    }
}
