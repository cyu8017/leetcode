// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

object Solution {
  def waysToPartition(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val pref = Array.ofDim[Long](n)
    pref(0) = nums(0)
    var i = 1
    while (i < n) { pref(i) = pref(i - 1) + nums(i); i += 1 }
    val total = pref(n - 1)
    val right = scala.collection.mutable.Map.empty[Long, Int]
    val left = scala.collection.mutable.Map.empty[Long, Int]
    i = 0
    while (i < n - 1) {
      right(pref(i)) = right.getOrElse(pref(i), 0) + 1
      i += 1
    }
    var ans = 0
    if (total % 2 == 0) ans = right.getOrElse(total / 2, 0)
    i = 0
    while (i < n) {
      val diff = k.toLong - nums(i)
      val newTotal = total + diff
      var cur = 0
      if (newTotal % 2 == 0) {
        val half = newTotal / 2
        cur = left.getOrElse(half, 0) + right.getOrElse(half - diff, 0)
      }
      ans = math.max(ans, cur)
      if (i < n - 1) {
        left(pref(i)) = left.getOrElse(pref(i), 0) + 1
        right(pref(i)) = right(pref(i)) - 1
      }
      i += 1
    }
    ans
  }
}
