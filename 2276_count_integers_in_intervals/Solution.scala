// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

class CountIntervals() {
  private class SegNode {
    var left: SegNode = null
    var right: SegNode = null
    var covered: Boolean = false
  }

  private var root: SegNode = null
  private var cnt: Int = 0

  private def addRange(L: Int, R: Int, l: Int, r: Int, node0: SegNode): (Int, SegNode) = {
    var node = node0
    if (node == null) node = new SegNode
    if (node.covered) return (0, node)
    if (l <= L && R <= r) {
      node.covered = true
      node.left = null
      node.right = null
      return (R - L + 1, node)
    }
    val mid = (L + R) / 2
    var added = 0
    if (l <= mid) {
      val res = addRange(L, mid, l, r, node.left)
      added += res._1
      node.left = res._2
    }
    if (r > mid) {
      val res = addRange(mid + 1, R, l, r, node.right)
      added += res._1
      node.right = res._2
    }
    if (node.left != null && node.right != null && node.left.covered && node.right.covered) {
      node.covered = true
      node.left = null
      node.right = null
    }
    (added, node)
  }

  def add(left: Int, right: Int): Unit = {
    val res = addRange(1, 1000000000, left, right, root)
    cnt += res._1
    root = res._2
  }

  def count(): Int = cnt
}
