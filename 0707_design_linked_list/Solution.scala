// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

class MyLinkedList() {
  private class Node(var value: Int, var next: Node = null)

  private val dummy = new Node(0)
  private var size = 0

  def get(index: Int): Int = {
    if (index < 0 || index >= size) return -1
    var node = dummy.next
    var i = 0
    while (i < index) {
      node = node.next
      i += 1
    }
    node.value
  }

  def addAtHead(`val`: Int): Unit = addAtIndex(0, `val`)

  def addAtTail(`val`: Int): Unit = addAtIndex(size, `val`)

  def addAtIndex(index: Int, `val`: Int): Unit = {
    if (index < 0 || index > size) return
    var prev = dummy
    var i = 0
    while (i < index) {
      prev = prev.next
      i += 1
    }
    val node = new Node(`val`)
    node.next = prev.next
    prev.next = node
    size += 1
  }

  def deleteAtIndex(index: Int): Unit = {
    if (index < 0 || index >= size) return
    var prev = dummy
    var i = 0
    while (i < index) {
      prev = prev.next
      i += 1
    }
    prev.next = prev.next.next
    size -= 1
  }
}
