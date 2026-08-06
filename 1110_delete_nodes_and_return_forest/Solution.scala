// LeetCode 1110 - Delete Nodes And Return Forest
// https://leetcode.com/problems/delete-nodes-and-return-forest/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def delNodes(root: TreeNode, to_delete: Array[Int]): List[TreeNode] = {
    val delete = to_delete.toSet
    val forest = scala.collection.mutable.ListBuffer.empty[TreeNode]

    def dfs(node: TreeNode, isRoot: Boolean): TreeNode = {
      if (node == null) return null
      val removed = delete.contains(node.value)
      if (isRoot && !removed) forest += node
      node.left = dfs(node.left, removed)
      node.right = dfs(node.right, removed)
      if (removed) null else node
    }

    dfs(root, true)
    forest.toList
  }
}
