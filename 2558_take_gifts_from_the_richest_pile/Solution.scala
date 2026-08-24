// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

object Solution {
  def pickGifts(gifts: Array[Int], k: Int): Long = {
    val h = scala.collection.mutable.PriorityQueue.empty[Int]
    gifts.foreach(g => h.enqueue(g))
    var i = 0
    while (i < k) {
      val x = h.dequeue()
      h.enqueue(math.sqrt(x.toDouble).toInt)
      i += 1
    }
    var ans = 0L
    while (h.nonEmpty) ans += h.dequeue()
    ans
  }
}
