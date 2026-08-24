// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

object Solution {
  def maximumSum(nums: Array[Int]): Int = {
    val best = scala.collection.mutable.Map.empty[Int, Int]
    var ans = -1
    nums.foreach { x =>
      val ds = digitSum(x)
      if (best.contains(ds)) {
        ans = math.max(ans, best(ds) + x)
        if (x > best(ds)) best(ds) = x
      } else {
        best(ds) = x
      }
    }
    ans
  }

  private def digitSum(x0: Int): Int = {
    var x = x0
    var s = 0
    while (x > 0) {
      s += x % 10
      x /= 10
    }
    s
  }
}
