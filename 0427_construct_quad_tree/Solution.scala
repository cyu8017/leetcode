// LeetCode 0427 - Construct Quad Tree
// https://leetcode.com/problems/construct-quad-tree/

class Node(
  _val: Boolean = false,
  _isLeaf: Boolean = false,
  _topLeft: Node = null,
  _topRight: Node = null,
  _bottomLeft: Node = null,
  _bottomRight: Node = null,
) {
  var value: Boolean = _val
  var isLeaf: Boolean = _isLeaf
  var topLeft: Node = _topLeft
  var topRight: Node = _topRight
  var bottomLeft: Node = _bottomLeft
  var bottomRight: Node = _bottomRight
}

object Solution {
  def construct(grid: Array[Array[Int]]): Node = {
    def build(row: Int, col: Int, size: Int): Node = {
      if (size == 1) {
        return new Node(grid(row)(col) == 1, true)
      }

      val half = size / 2
      val topLeft = build(row, col, half)
      val topRight = build(row, col + half, half)
      val bottomLeft = build(row + half, col, half)
      val bottomRight = build(row + half, col + half, half)

      if (
        topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf &&
        topLeft.value == topRight.value && topLeft.value == bottomLeft.value &&
        topLeft.value == bottomRight.value
      ) {
        return new Node(topLeft.value, true)
      }

      new Node(true, false, topLeft, topRight, bottomLeft, bottomRight)
    }

    build(0, 0, grid.length)
  }
}
