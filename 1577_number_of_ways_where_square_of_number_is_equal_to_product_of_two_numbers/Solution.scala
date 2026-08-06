// LeetCode 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
// https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

object Solution {
  def numTriplets(nums1: Array[Int], nums2: Array[Int]): Int = {
    def count(a: Array[Int], b: Array[Int]): Int = {
      val squares = scala.collection.mutable.Map.empty[Long, Int]
      for (x <- a) {
        val sq = x.toLong * x
        squares(sq) = squares.getOrElse(sq, 0) + 1
      }
      val products = scala.collection.mutable.Map.empty[Long, Int]
      for (i <- b.indices; j <- i + 1 until b.length) {
        val p = b(i).toLong * b(j)
        products(p) = products.getOrElse(p, 0) + 1
      }
      squares.map { case (value, c) => c * products.getOrElse(value, 0) }.sum
    }
    count(nums1, nums2) + count(nums2, nums1)
  }
}
