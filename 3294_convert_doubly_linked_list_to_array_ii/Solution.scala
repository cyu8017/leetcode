// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

class Node(var x: Int = 0, var prev: Node = null, var next: Node = null)

object Solution {
  def toArray(node: Node): Array[Int] = {
    var cur = node
    while (cur != null && cur.prev != null) cur = cur.prev
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    while (cur != null) {
      ans += cur.x
      cur = cur.next
    }
    ans.toArray
  }
}
