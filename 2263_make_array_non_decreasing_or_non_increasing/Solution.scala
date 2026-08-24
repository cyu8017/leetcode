// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

object Solution {
  def convertArray(nums: Array[Int]): Int = {
    def cost(arr: Array[Int]): Int = {
      val h = scala.collection.mutable.PriorityQueue.empty[Int]
      var ans = 0
      for (x <- arr) {
        if (h.nonEmpty && h.head > x) {
          val t = h.dequeue()
          ans += t - x
          h.enqueue(x)
        }
        h.enqueue(x)
      }
      ans
    }
    val rev = new Array[Int](nums.length)
    var i = 0
    while (i < nums.length) {
      rev(i) = nums(nums.length - 1 - i)
      i += 1
    }
    math.min(cost(nums), cost(rev))
  }
}
