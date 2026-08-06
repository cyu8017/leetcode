// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

object Solution {
  def connectSticks(sticks: Array[Int]): Int = {
    if (sticks.length <= 1) return 0
    val pq = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
    sticks.foreach(pq.enqueue(_))
    var ans = 0
    while (pq.size > 1) {
      val cost = pq.dequeue() + pq.dequeue()
      ans += cost
      pq.enqueue(cost)
    }
    ans
  }
}
