// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/

import scala.collection.mutable

object Solution {
  def exclusiveTime(n: Int, logs: List[String]): Array[Int] = {
    val result = Array.fill(n)(0)
    val stack = mutable.ArrayBuffer.empty[Int]
    var prevTime = 0
    logs.foreach { log =>
      val parts = log.split(":")
      val funcId = parts(0).toInt
      val event = parts(1)
      val time = parts(2).toInt
      if (event == "start") {
        if (stack.nonEmpty) result(stack.last) += time - prevTime
        stack += funcId
        prevTime = time
      } else {
        result(stack.remove(stack.size - 1)) += time - prevTime + 1
        prevTime = time + 1
      }
    }
    result
  }
}
