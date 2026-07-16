// LeetCode 0109 - Convert Sorted List to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun sortedListToBST(head: ListNode?): TreeNode? {
        val values = mutableListOf<Int>()
        var current = head
        while (current != null) {
            values.add(current.`val`)
            current = current.next
        }
        return build(values, 0, values.size - 1)
    }

    private fun build(values: List<Int>, left: Int, right: Int): TreeNode? {
        if (left > right) {
            return null
        }
        val mid = (left + right + 1) / 2
        val root = TreeNode(values[mid])
        root.left = build(values, left, mid - 1)
        root.right = build(values, mid + 1, right)
        return root
    }
}
