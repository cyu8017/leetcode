// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

object Solution {
  def minimumSeconds(nums: List[Int]): Int = {
    val n = nums.length
    val pos = scala.collection.mutable.LinkedHashMap.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < n) {
      val buf = pos.getOrElseUpdate(nums(i), scala.collection.mutable.ArrayBuffer.empty[Int])
      buf += i
      i += 1
    }
    var ans = n
    pos.values.foreach { p =>
      var maxGap = 0
      i = 0
      while (i < p.length) {
        val gap = if (i + 1 < p.length) p(i + 1) - p(i) else p(0) + n - p(i)
        maxGap = math.max(maxGap, gap / 2)
        i += 1
      }
      ans = math.min(ans, maxGap)
    }
    ans
  }
}
