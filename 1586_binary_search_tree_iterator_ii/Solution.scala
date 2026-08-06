// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

class BSTIterator(_root: TreeNode) {
  private val values = scala.collection.mutable.ArrayBuffer.empty[Int]
  private var index = -1
  {
    val stack = scala.collection.mutable.Stack.empty[TreeNode]
    var root = _root
    while (stack.nonEmpty || root != null) {
      while (root != null) {
        stack.push(root)
        root = root.left
      }
      root = stack.pop()
      values += root.value
      root = root.right
    }
  }

  def hasNext(): Boolean = index + 1 < values.length
  def next(): Int = { index += 1; values(index) }
  def hasPrev(): Boolean = index > 0
  def prev(): Int = { index -= 1; values(index) }
}
