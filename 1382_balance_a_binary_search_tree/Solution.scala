class TreeNode(var value: Int = 0, var left: TreeNode = null, var right: TreeNode = null)
object Solution {
  def balanceBST(root: TreeNode): TreeNode = {
    val nodes = scala.collection.mutable.ArrayBuffer[TreeNode]()
    def walk(x: TreeNode): Unit = if (x != null) { walk(x.left); nodes += x; walk(x.right) }
    def build(l: Int, r: Int): TreeNode = if (l >= r) null else { val m = (l + r) / 2; val x = nodes(m); x.left = build(l, m); x.right = build(m + 1, r); x }
    walk(root); build(0, nodes.length)
  }
}
