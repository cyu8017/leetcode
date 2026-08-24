// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

object Solution {
  def edgeScore(edges: Array[Int]): Int = {
    val n = edges.length
    val score = Array.fill(n)(0L)
    var i = 0
    while (i < n) {
      score(edges(i)) += i
      i += 1
    }
    var ans = 0
    i = 1
    while (i < n) {
      if (score(i) > score(ans)) ans = i
      i += 1
    }
    ans
  }
}
