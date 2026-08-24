// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

object Solution {
  def makePrefSumNonNegative(nums: Array[Int]): Int = {
    val h = scala.collection.mutable.PriorityQueue.empty[Int](Ordering[Int].reverse)
    var sum = 0L
    var ans = 0
    nums.foreach { x =>
      sum += x
      if (x < 0) h.enqueue(x)
      if (sum < 0) {
        val worst = h.dequeue()
        sum -= worst
        ans += 1
      }
    }
    ans
  }
}
