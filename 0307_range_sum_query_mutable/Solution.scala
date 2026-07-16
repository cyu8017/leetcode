// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

class NumArray(nums: Array[Int]) {
  private val nums = nums.clone()
  private val tree = new Array[Int](nums.length + 1)

  for (index <- nums.indices) {
    add(index + 1, nums(index))
  }

  def update(index: Int, `val`: Int): Unit = {
    val delta = `val` - nums(index)
    nums(index) = `val`
    add(index + 1, delta)
  }

  def sumRange(left: Int, right: Int): Int = {
    prefix(right + 1) - prefix(left)
  }

  private def add(index: Int, delta: Int): Unit = {
    var current = index
    while (current <= nums.length) {
      tree(current) += delta
      current += current & -current
    }
  }

  private def prefix(index: Int): Int = {
    var total = 0
    var current = index
    while (current > 0) {
      total += tree(current)
      current -= current & -current
    }
    total
  }
}
