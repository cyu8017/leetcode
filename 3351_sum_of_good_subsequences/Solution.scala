// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

object Solution {
  def sumOfGoodSubsequences(nums: Array[Int]): Int = {
    val mod = 1000000007
    val cnt = scala.collection.mutable.HashMap.empty[Int, Int]
    val sum = scala.collection.mutable.HashMap.empty[Int, Int]
    var ans = 0
    for (x <- nums) {
      var c = 1
      var s = x
      if (cnt.getOrElse(x - 1, 0) > 0) {
        c = (c + cnt(x - 1)) % mod
        s = ((s.toLong + sum(x - 1) + cnt(x - 1).toLong * x % mod) % mod).toInt
      }
      if (cnt.getOrElse(x + 1, 0) > 0) {
        c = (c + cnt(x + 1)) % mod
        s = ((s.toLong + sum(x + 1) + cnt(x + 1).toLong * x % mod) % mod).toInt
      }
      cnt(x) = (cnt.getOrElse(x, 0) + c) % mod
      sum(x) = (sum.getOrElse(x, 0) + s) % mod
      ans = (ans + s) % mod
    }
    ans
  }
}
