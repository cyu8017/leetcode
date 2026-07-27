// LeetCode 1606 - Find Servers That Handled Most Number of Requests
// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

import scala.collection.mutable

object Solution {
  def busiestServers(k: Int, arrival: Array[Int], load: Array[Int]): Array[Int] = {
    val free = mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
    (0 until k).foreach(i => free.enqueue(i))
    val busy = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._1).reverse)
    val count = Array.fill(k)(0)
    arrival.indices.foreach { i =>
      val t = arrival(i)
      while (busy.nonEmpty && busy.head._1 <= t) {
        val (_, server) = busy.dequeue()
        free.enqueue(i + ((server - i) % k + k) % k)
      }
      if (free.nonEmpty) {
        val server = free.dequeue() % k
        count(server) += 1
        busy.enqueue((t + load(i), server))
      }
    }
    val best = count.max
    count.indices.filter(count(_) == best).toArray
  }
}
