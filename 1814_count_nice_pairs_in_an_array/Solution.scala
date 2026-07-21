// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

object Solution {
  def countNicePairs(nums: Array[Int]): Int = {
    val MOD = 1000000007
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0
    for (num <- nums) {
      val diff = num - rev(num)
      ans = (ans + freq.getOrElse(diff, 0)) % MOD
      freq(diff) = freq.getOrElse(diff, 0) + 1
    }
    ans
  }

  private def rev(x: Int): Int = x.toString.reverse.toInt
}
