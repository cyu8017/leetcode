// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

class Node(_value: Int = 0, _children: List[Node] = Nil) {
  var value: Int = _value
  var children: List[Node] = _children
}

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def encodeNaryTree(root: Node): TreeNode = {
    if (root == null) {
      return null
    }

    val binary = new TreeNode(root.value)
    if (root.children.isEmpty) {
      return binary
    }

    binary.left = encodeNaryTree(root.children.head)
    var sibling = binary.left
    for (child <- root.children.tail) {
      sibling.right = encodeNaryTree(child)
      sibling = sibling.right
    }
    binary
  }

  def decodeBinaryTree(root: TreeNode): Node = {
    if (root == null) {
      return null
    }

    val node = new Node(root.value, Nil)
    var current = root.left
    while (current != null) {
      node.children = node.children :+ decodeBinaryTree(current)
      current = current.right
    }
    node
  }
}
