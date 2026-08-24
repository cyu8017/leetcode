// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def printTree(root: TreeNode): List[List[String]] = {
    val h = height(root)
    val rows = h + 1
    val cols = (1 << (h + 1)) - 1
    val res = mutable.ArrayBuffer.fill(rows)(mutable.ArrayBuffer.fill(cols)(""))
    place(root, 0, (cols - 1) / 2, h, res)
    res.map(_.toList).toList
  }

  private def height(node: TreeNode): Int = {
    if (node == null) return -1
    1 + math.max(height(node.left), height(node.right))
  }

  private def place(
    node: TreeNode,
    r: Int,
    c: Int,
    h: Int,
    res: mutable.ArrayBuffer[mutable.ArrayBuffer[String]],
  ): Unit = {
    if (node == null) return
    res(r)(c) = node.value.toString
    if (r == h) return
    val offset = 1 << (h - r - 1)
    place(node.left, r + 1, c - offset, h, res)
    place(node.right, r + 1, c + offset, h, res)
  }
}
