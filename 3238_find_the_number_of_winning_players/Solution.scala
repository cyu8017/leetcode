// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

object Solution {
  def winningPlayerCount(n: Int, pick: Array[Array[Int]]): Int = {
    val cnt = Array.ofDim[Int](n, 11)
    val s = scala.collection.mutable.HashSet.empty[Int]
    for (p <- pick) {
      val x = p(0)
      val y = p(1)
      cnt(x)(y) += 1
      if (cnt(x)(y) > x) s += x
    }
    s.size
  }
}
