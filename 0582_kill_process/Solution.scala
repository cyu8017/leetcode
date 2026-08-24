// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

import scala.collection.mutable

object Solution {
  def killProcess(pid: List[Int], ppid: List[Int], kill: Int): List[Int] = {
    val children = mutable.Map.empty[Int, mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < pid.size) {
      children.getOrElseUpdate(ppid(i), mutable.ArrayBuffer.empty[Int]) += pid(i)
      i += 1
    }
    val result = mutable.ArrayBuffer.empty[Int]
    val queue = mutable.Queue[Int](kill)
    while (queue.nonEmpty) {
      val process = queue.dequeue()
      result += process
      children.get(process).foreach(_.foreach(queue.enqueue))
    }
    result.toList
  }
}
