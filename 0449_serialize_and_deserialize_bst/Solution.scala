// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

class Codec {
  def serialize(root: TreeNode): String = {
    val parts = mutable.ListBuffer.empty[String]

    def preorder(node: TreeNode): Unit = {
      if (node == null) {
        parts += "#"
      } else {
        parts += node.value.toString
        preorder(node.left)
        preorder(node.right)
      }
    }

    preorder(root)
    parts.mkString(",")
  }

  def deserialize(data: String): TreeNode = {
    if (data == null || data.isEmpty) {
      return null
    }
    val values = data.split(",").iterator

    def build(): TreeNode = {
      val token = values.next()
      if (token == "#") {
        null
      } else {
        val node = new TreeNode(token.toInt)
        node.left = build()
        node.right = build()
        node
      }
    }

    build()
  }
}
