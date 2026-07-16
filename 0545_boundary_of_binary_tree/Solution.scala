// LeetCode 0545 - Boundary of Binary Tree
// https://leetcode.com/problems/boundary-of-binary-tree/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def boundaryOfBinaryTree(root: TreeNode): List[Int] = {
    if (root == null) {
      return Nil
    }
    if (isLeaf(root)) {
      return List(root.value)
    }

    List(root.value) ++ leftBoundary(root.left) ++ leaves(root) ++ rightBoundary(root.right)
  }

  private def isLeaf(node: TreeNode): Boolean = {
    node != null && node.left == null && node.right == null
  }

  private def leftBoundary(node: TreeNode): List[Int] = {
    if (node == null || isLeaf(node)) {
      Nil
    } else if (node.left != null) {
      node.value :: leftBoundary(node.left)
    } else {
      node.value :: leftBoundary(node.right)
    }
  }

  private def rightBoundary(node: TreeNode): List[Int] = {
    if (node == null || isLeaf(node)) {
      Nil
    } else if (node.right != null) {
      rightBoundary(node.right) :+ node.value
    } else {
      rightBoundary(node.left) :+ node.value
    }
  }

  private def leaves(node: TreeNode): List[Int] = {
    if (node == null) {
      Nil
    } else if (isLeaf(node)) {
      List(node.value)
    } else {
      leaves(node.left) ++ leaves(node.right)
    }
  }
}
