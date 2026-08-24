// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

object Solution {
  def isNStraightHand(hand: Array[Int], groupSize: Int): Boolean = {
    if (hand.length % groupSize != 0) return false
    val count = scala.collection.mutable.TreeMap.empty[Int, Int]
    hand.foreach { x => count(x) = count.getOrElse(x, 0) + 1 }
    while (count.nonEmpty) {
      val start = count.firstKey
      var x = start
      while (x < start + groupSize) {
        count.get(x) match {
          case None => return false
          case Some(1) => count.remove(x)
          case Some(c) => count(x) = c - 1
        }
        x += 1
      }
    }
    true
  }
}
