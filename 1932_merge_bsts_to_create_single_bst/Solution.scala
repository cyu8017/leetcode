// LeetCode 1932 - Merge BSTs to Create Single BST
// https://leetcode.com/problems/merge-bsts-to-create-single-bst/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def canMerge(trees: List[TreeNode]): TreeNode = {
    val valueToRoot = scala.collection.mutable.Map.empty[Int, TreeNode]
    val count = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
    for (tree <- trees) {
      valueToRoot(tree.value) = tree
      count(tree.value) += 1
      if (tree.left != null) count(tree.left.value) += 1
      if (tree.right != null) count(tree.right.value) += 1
    }
    val roots = trees.filter(t => count(t.value) == 1)
    if (roots.length != 1) return null
    val root = roots.head

    def merge(node: TreeNode): Boolean = {
      if (node == null) return true
      if (node.left != null && valueToRoot.contains(node.left.value)) {
        node.left = valueToRoot.remove(node.left.value).get
      }
      if (node.right != null && valueToRoot.contains(node.right.value)) {
        node.right = valueToRoot.remove(node.right.value).get
      }
      merge(node.left) && merge(node.right)
    }

    valueToRoot.remove(root.value)
    if (!merge(root) || valueToRoot.nonEmpty) return null

    def isValidBst(node: TreeNode, lo: Long, hi: Long): Boolean = {
      if (node == null) return true
      if (node.value <= lo || node.value >= hi) return false
      isValidBst(node.left, lo, node.value) && isValidBst(node.right, node.value, hi)
    }

    if (isValidBst(root, Long.MinValue, Long.MaxValue)) root else null
  }
}
