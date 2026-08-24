// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

object Solution {
  def sumOfPower(nums: Array[Int]): Int = {
    val MOD = 1000000007
    scala.util.Sorting.quickSort(nums)
    var ans = 0L
    var s = 0L
    var i = 0
    while (i < nums.length) {
      val x = nums(i).toLong
      ans = (ans + (s + x) % MOD * x % MOD * x) % MOD
      s = (s * 2 + x) % MOD
      i += 1
    }
    ans.toInt
  }
}
