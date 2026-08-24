// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

object Solution {
  def countHighestScoreNodes(parents: Array[Int]): Int = {
    val n = parents.length
    val children = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) { children(parents(i)) += i; i += 1 }
    val size = Array.ofDim[Int](n)
    def dfs(u: Int): Int = {
      size(u) = 1
      children(u).foreach { v => size(u) += dfs(v) }
      size(u)
    }
    dfs(0)
    var best = 0L
    var ans = 0
    var u = 0
    while (u < n) {
      var score = 1L
      children(u).foreach { v => score *= size(v) }
      val up = n - size(u)
      if (up > 0) score *= up
      if (score > best) { best = score; ans = 1 }
      else if (score == best) ans += 1
      u += 1
    }
    ans
  }
}
