// LeetCode 0109 - Convert Sorted List to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

class ListNode(var x: Int = 0) {
  var next: ListNode = null
}

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def sortedListToBST(head: ListNode): TreeNode = {
    val values = scala.collection.mutable.ArrayBuffer[Int]()
    var current = head
    while (current != null) {
      values += current.x
      current = current.next
    }

    def build(left: Int, right: Int): TreeNode = {
      if (left > right) {
        null
      } else {
        val mid = (left + right + 1) / 2
        val root = new TreeNode(values(mid))
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        root
      }
    }

    build(0, values.length - 1)
  }
}
