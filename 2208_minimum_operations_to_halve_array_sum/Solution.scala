// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

object Solution {
  def halveArray(nums: Array[Int]): Int = {
    val h = scala.collection.mutable.PriorityQueue.empty[Double]
    var sum = 0.0
    for (x <- nums) {
      h.enqueue(x.toDouble)
      sum += x
    }
    val target = sum / 2.0
    var ans = 0
    while (sum > target) {
      val top = h.dequeue()
      val x = top / 2.0
      sum -= x
      h.enqueue(x)
      ans += 1
    }
    ans
  }
}
