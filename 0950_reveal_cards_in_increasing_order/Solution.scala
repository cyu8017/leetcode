// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

object Solution {
  def deckRevealedIncreasing(deck: Array[Int]): Array[Int] = {
    val sorted = deck.sorted
    val n = sorted.length
    val idx = scala.collection.mutable.ArrayDeque[Int]()
    var i = 0
    while (i < n) { idx.append(i); i += 1 }
    val ans = Array.ofDim[Int](n)
    sorted.foreach { card =>
      ans(idx.removeHead()) = card
      if (idx.nonEmpty) idx.append(idx.removeHead())
    }
    ans
  }
}
