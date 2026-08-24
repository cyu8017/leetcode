// LeetCode 0558 - Logical OR of Two Binary Grids Represented as Quad-Trees
// https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

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
  def intersect(quadTree1: Node, quadTree2: Node): Node = {
    if (quadTree1.isLeaf) {
      if (quadTree1.value) quadTree1 else quadTree2
    } else if (quadTree2.isLeaf) {
      if (quadTree2.value) quadTree2 else quadTree1
    } else {
      val topLeft = intersect(quadTree1.topLeft, quadTree2.topLeft)
      val topRight = intersect(quadTree1.topRight, quadTree2.topRight)
      val bottomLeft = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
      val bottomRight = intersect(quadTree1.bottomRight, quadTree2.bottomRight)
      if (topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf
          && topLeft.value == topRight.value && topRight.value == bottomLeft.value
          && bottomLeft.value == bottomRight.value) {
        new Node(topLeft.value, true)
      } else {
        new Node(false, false, topLeft, topRight, bottomLeft, bottomRight)
      }
    }
  }
}
