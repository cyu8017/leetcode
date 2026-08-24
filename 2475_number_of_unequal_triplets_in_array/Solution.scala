// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

object Solution {
  def unequalTriplets(nums: Array[Int]): Int = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var i = 0
    while (i < nums.length) {
      cnt(nums(i)) = cnt.getOrElse(nums(i), 0) + 1
      i += 1
    }
    var ans = 0
    val n = nums.length
    var left = 0
    cnt.values.foreach { c =>
      val right = n - left - c
      ans += left * c * right
      left += c
    }
    ans
  }
}
