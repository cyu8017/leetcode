import scala.collection.mutable

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

class BSTIterator(root: TreeNode) {
  private val stack = mutable.Stack[TreeNode]()
  pushLeft(root)

  def next(): Int = {
    val node = stack.pop()
    pushLeft(node.right)
    node.value
  }

  def hasNext(): Boolean = stack.nonEmpty

  private def pushLeft(start: TreeNode): Unit = {
    var node = start
    while (node != null) {
      stack.push(node)
      node = node.left
    }
  }
}
