// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

object Solution {
  def checkArithmeticSubarrays(nums: Array[Int], l: Array[Int], r: Array[Int]): List[Boolean] = {
    l.indices.map { i =>
      val x = nums.slice(l(i), r(i) + 1).sorted
      x.length < 3 || (1 until x.length).forall(j => x(j) - x(j - 1) == x(1) - x(0))
    }.toList
  }
}
