// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

class SparseVector(nums: Array[Int]) {
  val values: Map[Int, Int] = nums.zipWithIndex.collect { case (x, i) if x != 0 => i -> x }.toMap

  def dotProduct(vec: SparseVector): Int = {
    if (values.size > vec.values.size) return vec.dotProduct(this)
    values.map { case (i, x) => x * vec.values.getOrElse(i, 0) }.sum
  }
}

object Solution {
  def dotProduct(nums1: Array[Int], nums2: Array[Int]): Int =
    new SparseVector(nums1).dotProduct(new SparseVector(nums2))
}
