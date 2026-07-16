import scala.collection.mutable

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def rightSideView(root: TreeNode): List[Int] = {
    if (root == null) return List.empty[Int]
    val result = mutable.ListBuffer[Int]()
    val queue = mutable.Queue[TreeNode](root)
    while (queue.nonEmpty) {
      val size = queue.size
      for (index <- 0 until size) {
        val node = queue.dequeue()
        if (index == size - 1) result += node.value
        if (node.left != null) queue.enqueue(node.left)
        if (node.right != null) queue.enqueue(node.right)
      }
    }
    result.toList
  }
}
