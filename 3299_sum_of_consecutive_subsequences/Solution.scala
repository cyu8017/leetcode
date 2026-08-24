// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

object Solution {
  def rangeSum(nums: Array[Int]): Int = {
    val mod = 1000000007
    val cnt = scala.collection.mutable.HashMap.empty[Int, Int]
    val sum = scala.collection.mutable.HashMap.empty[Int, Int]
    var ans = 0
    for (x <- nums) {
      val cL = cnt.getOrElse(x - 1, 0)
      val sL = sum.getOrElse(x - 1, 0)
      val cR = cnt.getOrElse(x + 1, 0)
      val sR = sum.getOrElse(x + 1, 0)
      var c = (1 + cL + cR) % mod
      var s = ((x.toLong + sL + cL.toLong * x % mod + sR + cR.toLong * x % mod) % mod).toInt
      if (cL > 0 && cR > 0) {
        c = (c + (cL.toLong * cR % mod).toInt) % mod
        s = ((s + sL.toLong * cR % mod + sR.toLong * cL % mod + cL.toLong * cR % mod * x % mod) % mod).toInt
      }
      cnt(x) = (cnt.getOrElse(x, 0) + c) % mod
      sum(x) = (sum.getOrElse(x, 0) + s) % mod
      ans = (ans + s) % mod
    }
    ans
  }
}
