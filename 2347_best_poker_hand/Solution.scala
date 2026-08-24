// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

object Solution {
  def bestHand(ranks: Array[Int], suits: Array[Char]): String = {
    if (suits(0) == suits(1) && suits(1) == suits(2) && suits(2) == suits(3) && suits(3) == suits(4)) {
      return "Flush"
    }
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var best = 0
    ranks.foreach { r =>
      val c = cnt.getOrElse(r, 0) + 1
      cnt(r) = c
      best = math.max(best, c)
    }
    if (best >= 3) "Three of a Kind"
    else if (best == 2) "Pair"
    else "High Card"
  }
}
