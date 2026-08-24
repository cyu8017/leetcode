// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

class CBTInserter(_root: TreeNode) {
  private val root = _root
  private val parents = scala.collection.mutable.Queue[TreeNode]()

  {
    val q = scala.collection.mutable.Queue[TreeNode]()
    q.enqueue(root)
    var done = false
    while (q.nonEmpty && !done) {
      val node = q.dequeue()
      if (node.left != null) q.enqueue(node.left)
      else {
        parents.enqueue(node)
        done = true
      }
      if (!done) {
        if (node.right != null) q.enqueue(node.right)
        else {
          parents.enqueue(node)
          done = true
        }
      }
    }
    while (q.nonEmpty) parents.enqueue(q.dequeue())
  }

  def insert(`val`: Int): Int = {
    val parent = parents.front
    val child = new TreeNode(`val`)
    if (parent.left == null) parent.left = child
    else {
      parent.right = child
      parents.dequeue()
    }
    parents.enqueue(child)
    parent.value
  }

  def get_root(): TreeNode = root
  def getRoot(): TreeNode = root
}
