// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

object Solution {
  def minEliminationTime(timeReq: Array[Int], splitTime: Int): Long = {
    val pq = new java.util.PriorityQueue[Integer]()
    for (v <- timeReq) pq.offer(v)
    while (pq.size() > 1) {
      pq.poll()
      val x = pq.poll()
      pq.offer(x + splitTime)
    }
    pq.peek().toLong
  }
}
