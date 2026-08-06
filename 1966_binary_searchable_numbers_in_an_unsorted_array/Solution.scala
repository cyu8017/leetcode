// LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
// https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

object Solution {
  def binarySearchableNumbers(nums: Array[Int]): Int = {
    val n = nums.length
    val ok = Array.fill(n)(1)
    var mx = Int.MinValue
    for (i <- nums.indices) {
      if (nums(i) < mx) ok(i) = 0
      else mx = nums(i)
    }
    var mi = Int.MaxValue
    for (i <- n - 1 to 0 by -1) {
      if (nums(i) > mi) ok(i) = 0
      else mi = nums(i)
    }
    ok.sum
  }
}
