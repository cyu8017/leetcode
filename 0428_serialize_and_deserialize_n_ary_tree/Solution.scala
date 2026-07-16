// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

import scala.collection.mutable

class Node(_value: Int = 0, _children: List[Node] = Nil) {
  var value: Int = _value
  var children: List[Node] = _children
}

class Codec {
  def encode(root: Node): String = {
    if (root == null) {
      return ""
    }

    val parts = mutable.ListBuffer.empty[String]
    val queue = mutable.Queue.empty[Node]
    queue.enqueue(root)
    while (queue.nonEmpty) {
      val node = queue.dequeue()
      parts += node.value.toString
      parts += node.children.length.toString
      for (child <- node.children) {
        parts += child.value.toString
        queue.enqueue(child)
      }
    }
    parts.mkString(",")
  }

  def decode(data: String): Node = {
    if (data == null || data.isEmpty) {
      return null
    }

    val values = data.split(",")
    var index = 0

    def readRoot(): Node = {
      val value = values(index).toInt
      val childCount = values(index + 1).toInt
      index += 2
      val node = new Node(value, Nil)
      for (_ <- 0 until childCount) {
        node.children = node.children :+ new Node(values(index).toInt, Nil)
        index += 1
      }
      node
    }

    val root = readRoot()
    val queue = mutable.Queue.from(root.children)
    while (queue.nonEmpty) {
      val node = queue.dequeue()
      val value = values(index).toInt
      val childCount = values(index + 1).toInt
      index += 2
      require(value == node.value, s"expected node value ${node.value}, found $value")
      for (_ <- 0 until childCount) {
        val child = new Node(values(index).toInt, Nil)
        node.children = node.children :+ child
        queue.enqueue(child)
        index += 1
      }
    }
    root
  }
}
