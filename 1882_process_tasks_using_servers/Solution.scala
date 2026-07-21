// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

import scala.collection.mutable

object Solution {
  def assignTasks(servers: Array[Int], tasks: Array[Int]): Array[Int] = {
    val available = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), (Int, Int)](t => (t._1, t._2)).reverse)
    for (index <- servers.indices) {
      available.enqueue((servers(index), index))
    }
    val busy = mutable.PriorityQueue.empty[(Long, Int, Int)](
      Ordering.by[(Long, Int, Int), (Long, Int, Int)](t => (t._1, t._2, t._3)).reverse
    )
    val answer = Array.ofDim[Int](tasks.length)
    var time = 0L

    for (moment <- tasks.indices) {
      val task = tasks(moment)
      time = math.max(time, moment.toLong)
      while (busy.nonEmpty && busy.head._1 <= time) {
        val (_, weight, index) = busy.dequeue()
        available.enqueue((weight, index))
      }
      while (available.isEmpty) {
        time = busy.head._1
        while (busy.nonEmpty && busy.head._1 <= time) {
          val (_, weight, index) = busy.dequeue()
          available.enqueue((weight, index))
        }
      }
      val (weight, index) = available.dequeue()
      busy.enqueue((time + task, weight, index))
      answer(moment) = index
    }
    answer
  }
}
