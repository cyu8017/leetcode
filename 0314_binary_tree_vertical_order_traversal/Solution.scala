// LeetCode 0314 - Binary Tree Vertical Order Traversal

// https://leetcode.com/problems/binary-tree-vertical-order-traversal/



import scala.collection.mutable



class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {

  var value: Int = _value

  var left: TreeNode = _left

  var right: TreeNode = _right

}



object Solution {

  def verticalOrder(root: TreeNode): List[List[Int]] = {

    if (root == null) {

      return List.empty

    }



    val columns = mutable.Map.empty[Int, mutable.ListBuffer[Int]]

    val nodes = mutable.Queue.empty[TreeNode]

    val columnIndexes = mutable.Queue.empty[Int]

    nodes.enqueue(root)

    columnIndexes.enqueue(0)

    var minCol = 0

    var maxCol = 0



    while (nodes.nonEmpty) {

      val node = nodes.dequeue()

      val column = columnIndexes.dequeue()

      minCol = math.min(minCol, column)

      maxCol = math.max(maxCol, column)

      columns.getOrElseUpdate(column, mutable.ListBuffer.empty[Int]) += node.value

      if (node.left != null) {

        nodes.enqueue(node.left)

        columnIndexes.enqueue(column - 1)

      }

      if (node.right != null) {

        nodes.enqueue(node.right)

        columnIndexes.enqueue(column + 1)

      }

    }



    (minCol to maxCol).map(column => columns(column).toList).toList

  }

}

