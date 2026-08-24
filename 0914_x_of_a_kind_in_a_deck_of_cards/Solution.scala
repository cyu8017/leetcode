// LeetCode 0914 - X of a Kind in a Deck of Cards
// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

object Solution {
  def hasGroupsSizeX(deck: Array[Int]): Boolean = {
    val count = scala.collection.mutable.Map.empty[Int, Int]
    deck.foreach { x => count(x) = count.getOrElse(x, 0) + 1 }
    def gcd(a0: Int, b0: Int): Int = {
      var a = a0
      var b = b0
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    var g = 0
    count.values.foreach { c => g = gcd(g, c) }
    g >= 2
  }
}
