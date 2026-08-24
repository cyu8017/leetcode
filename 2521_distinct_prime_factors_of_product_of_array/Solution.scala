// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

object Solution {
  def distinctPrimeFactors(nums: Array[Int]): Int = {
    val set = scala.collection.mutable.Set.empty[Int]
    nums.foreach { num =>
      var x = num
      var p = 2
      while (p.toLong * p <= x) {
        if (x % p == 0) {
          set += p
          while (x % p == 0) x /= p
        }
        p += 1
      }
      if (x > 1) set += x
    }
    set.size
  }
}
