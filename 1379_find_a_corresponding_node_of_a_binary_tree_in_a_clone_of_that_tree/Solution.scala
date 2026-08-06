import scala.collection.mutable

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
object Solution {
  def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode): TreeNode = {
    val stack = mutable.Stack((original, cloned))
    while (stack.nonEmpty) { val (node, copy) = stack.pop(); if (node eq target) return copy; if (node.left != null) stack.push((node.left, copy.left)); if (node.right != null) stack.push((node.right, copy.right)) }
    null
  }
}
