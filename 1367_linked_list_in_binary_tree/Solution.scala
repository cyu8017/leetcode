class ListNode(_x: Int = 0, _next: ListNode = null) {
  var x: Int = _x
  var next: ListNode = _next
}
class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}
object Solution {
  def isSubPath(head: ListNode, root: TreeNode): Boolean = {
    def matches(node: ListNode, tree: TreeNode): Boolean =
      node == null || (tree != null && node.x == tree.value && (matches(node.next, tree.left) || matches(node.next, tree.right)))
    root != null && (matches(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right))
  }
}
