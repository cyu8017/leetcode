// LeetCode 1995 - Count Special Quadruplets
// https://leetcode.com/problems/count-special-quadruplets/

object Solution {
  def countQuadruplets(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    for (a <- 0 until n; b <- a + 1 until n; c <- b + 1 until n) {
      val s = nums(a) + nums(b) + nums(c)
      for (d <- c + 1 until n if nums(d) == s) ans += 1
    }
    ans
  }
}
