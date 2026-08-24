// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

class Node(var value: Int = 0, var next: Node = null)

object Solution {
  def insert(head: Node, insertVal: Int): Node = {
    val node = new Node(insertVal)
    if (head == null) {
      node.next = node
      return node
    }
    var cur = head
    while (cur.next != null && !(cur.next eq head)) cur = cur.next
    cur.next = head
    var prev = head
    var curr = head.next
    var looping = true
    while (looping) {
      if (prev.value <= insertVal && insertVal <= curr.value) looping = false
      else if (prev.value > curr.value && (insertVal >= prev.value || insertVal <= curr.value)) looping = false
      else {
        prev = curr
        curr = curr.next
        if (prev eq head) looping = false
      }
    }
    prev.next = node
    node.next = curr
    head
  }
}
