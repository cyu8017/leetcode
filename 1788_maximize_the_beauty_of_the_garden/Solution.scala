// LeetCode 1788 - Maximize the Beauty of the Garden
// https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

object Solution {
  def maximumBeauty(flowers: Array[Int]): Int = {
    val first = scala.collection.mutable.Map.empty[Int, Int]
    val prefix = new Array[Long](flowers.length + 1)
    for (i <- flowers.indices) {
      prefix(i + 1) = prefix(i) + math.max(flowers(i), 0)
    }
    var best = Long.MinValue
    for (i <- flowers.indices) {
      val value = flowers(i)
      first.get(value) match {
        case Some(left) =>
          val between = prefix(i) - prefix(left + 1)
          best = math.max(best, flowers(left).toLong + flowers(i) + between)
        case None =>
          first(value) = i
      }
    }
    best.toInt
  }
}
