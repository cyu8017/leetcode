// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

object Solution {
  def findWinners(matches: Array[Array[Int]]): List[List[Int]] = {
    val lose = scala.collection.mutable.HashMap.empty[Int, Int]
    val seen = scala.collection.mutable.HashSet.empty[Int]
    for (m <- matches) {
      seen += m(0)
      seen += m(1)
      lose(m(1)) = lose.getOrElse(m(1), 0) + 1
    }
    val zero = scala.collection.mutable.ListBuffer.empty[Int]
    val one = scala.collection.mutable.ListBuffer.empty[Int]
    for (p <- seen) {
      val L = lose.getOrElse(p, 0)
      if (L == 0) zero += p
      else if (L == 1) one += p
    }
    List(zero.sorted.toList, one.sorted.toList)
  }
}
