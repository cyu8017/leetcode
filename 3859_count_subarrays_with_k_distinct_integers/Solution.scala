// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

object Solution {
  private var nums: Array[Int] = _
  private var k: Int = _
  private var m: Int = _

  def countSubarrays(nums: Array[Int], k: Int, m: Int): Long = {
    this.nums = nums
    this.k = k
    this.m = m
    f(k) - f(k + 1)
  }

  private def f(lim: Int): Long = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0L
    var l = 0
    var t = 0
    nums.foreach { x =>
      val c = cnt.getOrElse(x, 0) + 1
      cnt(x) = c
      if (c == m) t += 1
      while (cnt.size >= lim && t >= k) {
        val y = nums(l)
        l += 1
        val cy = cnt(y) - 1
        if (cy == m - 1) t -= 1
        if (cy == 0) cnt.remove(y)
        else cnt(y) = cy
      }
      ans += l
    }
    ans
  }
}
