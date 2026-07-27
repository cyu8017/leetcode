// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

object Solution {
  def minimumDeviation(nums: Array[Int]): Int = {
    val pq = scala.collection.mutable.PriorityQueue[Int]()
    var mn = Int.MaxValue
    for (raw <- nums) {
      var x = raw
      if (x % 2 == 1) x *= 2
      if (x < mn) mn = x
      pq.enqueue(x)
    }
    var ans = Int.MaxValue
    var done = false
    while (!done) {
      val x = pq.dequeue()
      ans = math.min(ans, x - mn)
      if (x % 2 == 1) done = true
      else {
        val y = x / 2
        if (y < mn) mn = y
        pq.enqueue(y)
      }
    }
    ans
  }
}
