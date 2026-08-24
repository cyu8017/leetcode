// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

class Node(var `val`: Int = 0) {
    var prev: Node? = null
    var next: Node? = null
}

class Solution {
    fun toArray(node: Node?): IntArray {
        var cur = node
        while (cur != null && cur.prev != null) cur = cur.prev
        val ans = ArrayList<Int>()
        while (cur != null) {
            ans.add(cur.`val`)
            cur = cur.next
        }
        return ans.toIntArray()
    }
}
