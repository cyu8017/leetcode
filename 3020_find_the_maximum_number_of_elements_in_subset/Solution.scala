// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

object Solution {
  def maximumLength(nums: Array[Int]): Int = {
    val cnt = scala.collection.mutable.HashMap[Long, Int]()
    for (x <- nums) cnt(x.toLong) = cnt.getOrElse(x.toLong, 0) + 1
    val ones = cnt.getOrElse(1L, 0)
    var ans = ones - ((ones % 2) ^ 1)
    cnt.remove(1L)
    val keys = cnt.keys.toList
    for (start <- keys) {
      var x = start
      var t = 0
      while (cnt.getOrElse(x, 0) > 1) {
        x = x * x
        t += 2
      }
      if (cnt.getOrElse(x, 0) > 0) t += 1 else t -= 1
      ans = math.max(ans, t)
    }
    ans
  }
}
