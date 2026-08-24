// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

object Solution {
  def maximumSum(nums: Array[Int]): Long = {
    val n = nums.length
    val groups = scala.collection.mutable.Map.empty[Int, Long]
    var ans = 0L
    for (i <- 1 to n) {
      val sf = squareFree(i)
      val sum = groups.getOrElse(sf, 0L) + nums(i - 1)
      groups(sf) = sum
      if (sum > ans) ans = sum
    }
    ans
  }

  private def squareFree(x0: Int): Int = {
    var x = x0
    var res = 1
    var p = 2
    while (p * p <= x) {
      var cnt = 0
      while (x % p == 0) {
        x /= p
        cnt += 1
      }
      if (cnt % 2 == 1) res *= p
      p += 1
    }
    if (x > 1) res *= x
    res
  }
}
