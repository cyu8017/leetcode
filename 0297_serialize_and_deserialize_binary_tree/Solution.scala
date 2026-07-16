// LeetCode 0297 - Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

class Codec {
  def serialize(root: TreeNode): String = {
    if (root == null) {
      return ""
    }
    val values = mutable.ListBuffer.empty[String]
    val queue = mutable.Queue.empty[TreeNode]
    queue.enqueue(root)
    while (queue.nonEmpty) {
      val node = queue.dequeue()
      if (node == null) {
        values += ""
      } else {
        values += node.value.toString
        queue.enqueue(node.left)
        queue.enqueue(node.right)
      }
    }
    while (values.nonEmpty && values.last.isEmpty) {
      values.remove(values.length - 1)
    }
    values.mkString(",")
  }

  def deserialize(data: String): TreeNode = {
    if (data == null || data.isEmpty) {
      return null
    }
    val values = data.split(",", -1)
    val root = new TreeNode(values(0).toInt)
    val queue = mutable.Queue.empty[TreeNode]
    queue.enqueue(root)
    var index = 1
    while (queue.nonEmpty && index < values.length) {
      val node = queue.dequeue()
      if (index < values.length && values(index).nonEmpty) {
        node.left = new TreeNode(values(index).toInt)
        queue.enqueue(node.left)
      }
      index += 1
      if (index < values.length && values(index).nonEmpty) {
        node.right = new TreeNode(values(index).toInt)
        queue.enqueue(node.right)
      }
      index += 1
    }
    root
  }
}
