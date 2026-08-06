// LeetCode 1305 - All Elements In Two Binary Search Trees
// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def getAllElements(root1: TreeNode, root2: TreeNode): List[Int] = {
    def inorder(root: TreeNode): List[Int] = {
      if (root == null) Nil
      else inorder(root.left) ::: root.value :: inorder(root.right)
    }
    val a = inorder(root1)
    val b = inorder(root2)
    val answer = scala.collection.mutable.ArrayBuffer[Int]()
    var i = 0
    var j = 0
    while (i < a.length || j < b.length) {
      if (j == b.length || (i < a.length && a(i) <= b(j))) {
        answer += a(i)
        i += 1
      } else {
        answer += b(j)
        j += 1
      }
    }
    answer.toList
  }
}
