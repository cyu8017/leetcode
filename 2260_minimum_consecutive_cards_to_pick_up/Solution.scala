// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

object Solution {
  def minimumCardPickup(cards: Array[Int]): Int = {
    val last = scala.collection.mutable.HashMap.empty[Int, Int]
    var ans = -1
    var i = 0
    while (i < cards.length) {
      if (last.contains(cards(i))) {
        val diff = i - last(cards(i)) + 1
        if (ans == -1 || diff < ans) ans = diff
      }
      last(cards(i)) = i
      i += 1
    }
    ans
  }
}
