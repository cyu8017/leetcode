// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

object Solution {
  def timeTaken(arrival: Array[Int], state: Array[Int]): Array[Int] = {
    val n = arrival.length
    val ans = Array.fill(n)(0)
    val enter = scala.collection.mutable.Queue.empty[Int]
    val exitq = scala.collection.mutable.Queue.empty[Int]
    var i = 0
    var t = 0
    var prev = 1
    while (i < n || enter.nonEmpty || exitq.nonEmpty) {
      while (i < n && arrival(i) <= t) {
        if (state(i) == 0) enter.enqueue(i)
        else exitq.enqueue(i)
        i += 1
      }
      if (enter.isEmpty && exitq.isEmpty) {
        if (i < n) {
          t = arrival(i)
          prev = 1
        }
      } else {
        if (prev == 1) {
          if (exitq.nonEmpty) {
            ans(exitq.dequeue()) = t
            prev = 1
          } else {
            ans(enter.dequeue()) = t
            prev = 0
          }
        } else {
          if (enter.nonEmpty) {
            ans(enter.dequeue()) = t
            prev = 0
          } else {
            ans(exitq.dequeue()) = t
            prev = 1
          }
        }
        t += 1
      }
    }
    ans
  }
}
