// LeetCode 0303 - Range Sum Query - Immutable
// https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(nums: Array[Int]) {
  private val prefix = new Array[Int](nums.length + 1)

  for (index <- nums.indices) {
    prefix(index + 1) = prefix(index) + nums(index)
  }

  def sumRange(left: Int, right: Int): Int = {
    prefix(right + 1) - prefix(left)
  }
}
