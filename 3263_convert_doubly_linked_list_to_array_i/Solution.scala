// LeetCode 3263 - Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

class Node(var x: Int = 0, var prev: Node = null, var next: Node = null)

object Solution {
  def toArray(head: Node): Array[Int] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = head
    while (cur != null) {
      ans += cur.x
      cur = cur.next
    }
    ans.toArray
  }
}
