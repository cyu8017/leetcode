// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)

object Solution {
  def minimumOperations(root: TreeNode): Int = {
    if (root == null) return 0
    var ans = 0
    val q = scala.collection.mutable.Queue[TreeNode](root)
    while (q.nonEmpty) {
      val sz = q.size
      val vals = new Array[Int](sz)
      var i = 0
      while (i < sz) {
        val node = q.dequeue()
        vals(i) = node.value
        if (node.left != null) q.enqueue(node.left)
        if (node.right != null) q.enqueue(node.right)
        i += 1
      }
      val sorted = vals.clone()
      scala.util.Sorting.quickSort(sorted)
      val pos = scala.collection.mutable.Map.empty[Int, Int]
      i = 0
      while (i < sz) {
        pos(vals(i)) = i
        i += 1
      }
      i = 0
      while (i < sz) {
        if (vals(i) != sorted(i)) {
          val j = pos(sorted(i))
          val tmp = vals(i)
          vals(i) = vals(j)
          vals(j) = tmp
          pos(vals(j)) = j
          pos(vals(i)) = i
          ans += 1
        }
        i += 1
      }
    }
    ans
  }
}
