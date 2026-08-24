// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

object Solution {
  def dailyTemperatures(temperatures: Array[Int]): Array[Int] = {
    val answer = Array.fill(temperatures.length)(0)
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < temperatures.length) {
      while (stack.nonEmpty && temperatures(stack.last) < temperatures(i)) {
        val prev = stack.remove(stack.length - 1)
        answer(prev) = i - prev
      }
      stack += i
      i += 1
    }
    answer
  }
}
