class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
object Solution {
  def maxSumBST(root: TreeNode): Int = {
    var answer = 0
    def dfs(node: TreeNode): (Boolean, Int, Int, Int) = if (node == null) (true, Int.MaxValue, Int.MinValue, 0) else {
      val left = dfs(node.left); val right = dfs(node.right)
      if (left._1 && right._1 && left._3 < node.value && node.value < right._2) { val sum = left._4 + right._4 + node.value; answer = math.max(answer, sum); (true, math.min(left._2, node.value), math.max(right._3, node.value), sum) } else (false, 0, 0, 0)
    }
    dfs(root); answer
  }
}
