// LeetCode 0366 - Find Leaves of Binary Tree

// https://leetcode.com/problems/find-leaves-of-binary-tree/



import scala.collection.mutable



class TreeNode(var _value: Int) {

  var value: Int = _value

  var left: TreeNode = null

  var right: TreeNode = null

}



object Solution {

  def findLeaves(root: TreeNode): List[List[Int]] = {

    val layers = mutable.ArrayBuffer.empty[mutable.ArrayBuffer[Int]]

    dfs(root, layers)

    layers.map(_.toList).toList

  }



  private def dfs(node: TreeNode, layers: mutable.ArrayBuffer[mutable.ArrayBuffer[Int]]): Int = {

    if (node == null) return -1



    val height = math.max(dfs(node.left, layers), dfs(node.right, layers)) + 1

    while (layers.length <= height) {

      layers += mutable.ArrayBuffer.empty[Int]

    }

    layers(height) += node.value

    height

  }

}
