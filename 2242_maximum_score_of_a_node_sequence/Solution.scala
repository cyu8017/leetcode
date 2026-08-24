// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

object Solution {
  def maximumScore(scores: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = scores.length
    val top = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    var i = 0
    while (i < n) {
      for (v <- g(i)) {
        top(i) += v
        var j = top(i).length - 1
        while (j > 0) {
          if (scores(top(i)(j)) > scores(top(i)(j - 1))) {
            val tmp = top(i)(j)
            top(i)(j) = top(i)(j - 1)
            top(i)(j - 1) = tmp
          }
          j -= 1
        }
        if (top(i).length > 3) top(i).remove(3, top(i).length - 3)
      }
      i += 1
    }
    var ans = -1
    for (e <- edges) {
      val a = e(0)
      val b = e(1)
      for (c <- top(a) if c != b) {
        for (d <- top(b) if d != a && d != c) {
          ans = math.max(ans, scores(a) + scores(b) + scores(c) + scores(d))
        }
      }
    }
    ans
  }
}
