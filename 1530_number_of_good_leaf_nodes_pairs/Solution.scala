// LeetCode 1530 - Number of Good Leaf Nodes Pairs
// https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

object Solution {
  def countPairs(root: TreeNode, distance: Int): Int = {
    var answer = 0
    def dfs(node: TreeNode): List[Int] = {
      if (node == null) return Nil
      if (node.left == null && node.right == null) return List(1)
      val left = dfs(node.left)
      val right = dfs(node.right)
      for (a <- left; b <- right if a + b <= distance) answer += 1
      (left ++ right).map(_ + 1).filter(_ < distance)
    }
    dfs(root)
    answer
  }
}
