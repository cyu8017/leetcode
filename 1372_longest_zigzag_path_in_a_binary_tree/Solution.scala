class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
object Solution {
  def longestZigZag(root: TreeNode): Int = {
    var answer = 0
    def dfs(node: TreeNode): (Int, Int) = if (node == null) (-1, -1) else { val left = dfs(node.left); val right = dfs(node.right); val a = left._2 + 1; val b = right._1 + 1; answer = math.max(answer, math.max(a, b)); (a, b) }
    dfs(root); answer
  }
}
