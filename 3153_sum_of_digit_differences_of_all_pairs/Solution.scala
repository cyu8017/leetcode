// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

object Solution {
  def sumDigitDifferences(nums: Array[Int]): Long = {
    val n = nums.length
    val m = math.floor(math.log10(nums(0))).toInt + 1
    var ans = 0L
    val vals = nums.clone()
    var k = 0
    while (k < m) {
      val cnt = new Array[Int](10)
      var i = 0
      while (i < n) {
        cnt(vals(i) % 10) += 1
        vals(i) /= 10
        i += 1
      }
      cnt.foreach(v => ans += v.toLong * (n - v))
      k += 1
    }
    ans / 2
  }
}
