// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/

import scala.collection.mutable

object Solution {
  def cutOffTree(forest: List[List[Int]]): Int = {
    val trees = mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    while (i < forest.size) {
      var j = 0
      while (j < forest.head.size) {
        if (forest(i)(j) > 1) trees += Array(forest(i)(j), i, j)
        j += 1
      }
      i += 1
    }
    val sorted = trees.sortBy(_(0))
    var sr = 0
    var sc = 0
    var steps = 0
    sorted.foreach { tree =>
      val dist = bfs(forest, sr, sc, tree(1), tree(2))
      if (dist < 0) return -1
      steps += dist
      sr = tree(1)
      sc = tree(2)
    }
    steps
  }

  private def bfs(forest: List[List[Int]], sr: Int, sc: Int, tr: Int, tc: Int): Int = {
    if (sr == tr && sc == tc) return 0
    val m = forest.size
    val n = forest.head.size
    val seen = Array.ofDim[Boolean](m, n)
    val queue = mutable.Queue(Array(sr, sc, 0))
    seen(sr)(sc) = true
    val dirs = Array(Array(-1, 0), Array(1, 0), Array(0, -1), Array(0, 1))
    while (queue.nonEmpty) {
      val cur = queue.dequeue()
      val r = cur(0)
      val c = cur(1)
      val dist = cur(2)
      dirs.foreach { dir =>
        val nr = r + dir(0)
        val nc = c + dir(1)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !seen(nr)(nc) && forest(nr)(nc) != 0) {
          if (nr == tr && nc == tc) return dist + 1
          seen(nr)(nc) = true
          queue.enqueue(Array(nr, nc, dist + 1))
        }
      }
    }
    -1
  }
}
