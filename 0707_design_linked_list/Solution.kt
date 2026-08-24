// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

class MyLinkedList {
    private class Node(var `val`: Int) {
        var next: Node? = null
    }

    private val dummy = Node(0)
    private var size = 0

    fun get(index: Int): Int {
        if (index < 0 || index >= size) return -1
        var node = dummy.next
        for (i in 0 until index) node = node!!.next
        return node!!.`val`
    }

    fun addAtHead(`val`: Int) { addAtIndex(0, `val`) }

    fun addAtTail(`val`: Int) { addAtIndex(size, `val`) }

    fun addAtIndex(index: Int, `val`: Int) {
        if (index < 0 || index > size) return
        var prev = dummy
        for (i in 0 until index) prev = prev.next!!
        val node = Node(`val`)
        node.next = prev.next
        prev.next = node
        size++
    }

    fun deleteAtIndex(index: Int) {
        if (index < 0 || index >= size) return
        var prev = dummy
        for (i in 0 until index) prev = prev.next!!
        prev.next = prev.next!!.next
        size--
    }
}
