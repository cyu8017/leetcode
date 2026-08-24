// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

object Solution {
  def countBadPairs(nums: Array[Int]): Long = {
    val n = nums.length.toLong
    val total = n * (n - 1) / 2
    val freq = scala.collection.mutable.Map.empty[Int, Long]
    var good = 0L
    var i = 0
    while (i < nums.length) {
      val key = nums(i) - i
      good += freq.getOrElse(key, 0L)
      freq(key) = freq.getOrElse(key, 0L) + 1
      i += 1
    }
    total - good
  }
}
