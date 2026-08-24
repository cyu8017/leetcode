// LeetCode 3263 - Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

class Node(
    var `val`: Int = 0,
    var prev: Node? = null,
    var next: Node? = null,
)

class Solution {
    fun toArray(head: Node?): IntArray {
        val ans = ArrayList<Int>()
        var cur = head
        while (cur != null) {
            ans.add(cur.`val`)
            cur = cur.next
        }
        return ans.toIntArray()
    }
}
