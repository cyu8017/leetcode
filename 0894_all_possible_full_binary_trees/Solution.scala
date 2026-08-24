// LeetCode 0894 - All Possible Full Binary Trees
// https://leetcode.com/problems/all-possible-full-binary-trees/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def allPossibleFBT(n: Int): List[TreeNode] = {
    val memo = scala.collection.mutable.Map.empty[Int, List[TreeNode]]
    def build(nodes: Int): List[TreeNode] = {
      if (memo.contains(nodes)) return memo(nodes)
      if (nodes % 2 == 0) {
        memo(nodes) = Nil
        return Nil
      }
      if (nodes == 1) {
        val res = List(new TreeNode(0))
        memo(nodes) = res
        return res
      }
      val res = scala.collection.mutable.ListBuffer[TreeNode]()
      var left = 1
      while (left < nodes) {
        val right = nodes - 1 - left
        build(left).foreach { L =>
          build(right).foreach { R =>
            res += new TreeNode(0, L, R)
          }
        }
        left += 2
      }
      val out = res.toList
      memo(nodes) = out
      out
    }
    build(n)
  }
}
